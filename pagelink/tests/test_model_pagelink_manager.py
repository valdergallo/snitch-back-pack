# coding=utf-8
from django.contrib.auth.models import User
from django.test import TestCase

from pagelink.models import PageLink
from pagelink.tests.fixtures import create_default_links_and_users


class TestLinkManager(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls = create_default_links_and_users(cls)

    def test_link_for_user(self):
        links = PageLink.objects.for_user(user=self.user)
        assert links.count() == 1

    def test_link_for_admin_user(self):
        links = PageLink.objects.for_user(user=self.admin_user)
        assert links.count() == 2

    def test_link_for_other_user(self):
        links = PageLink.objects.for_user(user=self.other)
        assert links.count() == 0

    def test_if_user_has_perm(self):
        user = User.objects.get(id=self.user.id)
        assert user.has_perm('pagelink.' + self.user_permission)
