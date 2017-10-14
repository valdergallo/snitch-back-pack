# coding=utf-8
import pytest
from chance import chance
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from pagelink.models import PageLink
USER_PASSWORD = 'secret'


@pytest.fixture(scope="module")
@pytest.mark.django_db
def create_superuser():
    return User.objects.create_superuser(
        username=chance.name(),
        email=chance.email(),
        password=USER_PASSWORD
    )


@pytest.fixture(scope="module")
@pytest.mark.django_db
def create_user():
    return User.objects.create_user(
        username=chance.name(),
        email=chance.email(),
        password=USER_PASSWORD
    )


@pytest.fixture(scope="module")
@pytest.mark.django_db
def create_default_links_and_users(cls):
    cls.admin_user = create_superuser()
    cls.user = create_user()
    cls.other = create_user()
    cls.admin_permission = 'admin_perm'
    cls.user_permission = 'user_perm'
    cls.other_permission = 'other_perm'

    cls.no_link = PageLink.objects.create(
        url='none',
        display='noneLink'
    )
    cls.user_link = PageLink.objects.create(
        url='user',
        display='userLink'
    )
    cls.user_link.add_permission(name=cls.admin_permission)
    cls.user_link.add_permission(name=cls.user_permission)

    cls.admin_link = PageLink.objects.create(
        url='admin',
        display='adminLink'
    )
    cls.admin_link.add_permission(name=cls.admin_permission)

    cls.admin_user.user_permissions.add(
        Permission.objects.get(name=cls.admin_permission))

    cls.user.user_permissions.add(
        Permission.objects.get(name=cls.user_permission))

    return cls
