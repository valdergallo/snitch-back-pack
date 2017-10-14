# coding=utf-8
from django.db import models
from django.contrib.auth.models import Permission, User, ContentType
from django.utils.text import slugify
from rest_framework.authtoken.models import Token

class PageLinkManager(models.Manager):
    """
    Default filter to be used in Links
    """

    def for_user(self, user):
        """
        Return the links that the user can has access

        args:
            user: django.contrib.auth.models.User
        return:
            queryset: list
        """
        return self.filter(
            permissions__in=user.user_permissions.values_list('id', flat=True))


class PageLink(models.Model):
    """
    Provide the links with permissions to
    be used in site
    """
    url = models.CharField(max_length=150)
    display = models.CharField(max_length=150)
    permissions = models.ManyToManyField(Permission)

    objects = PageLinkManager()

    def __str__(self):
        return self.url

    def add_permission(self, name, code_name=None):
        """
        Add one Django Permission for one link
        """
        if not code_name:
            code_name = slugify(name)

        content_type, _ = ContentType.objects.get_or_create(
            app_label="pagelink", model="PageLink")

        permission, _ = Permission.objects.get_or_create(
            content_type=content_type,
            name=name,
            codename=code_name
        )
        return self.permissions.add(permission)


class PageLinkTracker(models.Model):
    """
    Track link usage by users
    """
    page_link = models.ForeignKey(PageLink)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_token(self):
        return Token.objects.get(user=self.user)

