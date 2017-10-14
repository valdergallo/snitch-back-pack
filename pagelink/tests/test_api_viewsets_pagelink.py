# coding=utf-8
from django.test import TestCase
from pagelink.tests.fixtures import (
    create_default_links_and_users, USER_PASSWORD)
from rest_framework.test import APIClient
from django.urls import reverse


class TestPageLinkViewSetPermission(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls = create_default_links_and_users(cls)

    def setUp(self):
        self.client = APIClient()

    def test_list_links_without_login(self):
        response = self.client.get(reverse('pagelink-list'))
        assert response.status_code == 403  # Forbidden

    def test_list_links_with_login(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )
        response = self.client.get(reverse('pagelink-list'))
        assert response.status_code == 200  # Success


class TestPageLinkViewSetData(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls = create_default_links_and_users(cls)

    def setUp(self):
        self.client = APIClient()

    def test_json_date_for_user(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )
        response = self.client.get(reverse('pagelink-list'))
        expected_data = [
            {'id': 2, 'url': 'user', 'display': 'userLink'}
        ]
        assert response.json() == expected_data

    def test_json_date_for_admin(self):
        self.client.login(
            username=self.admin_user.username,
            password=USER_PASSWORD
        )
        response = self.client.get(reverse('pagelink-list'))
        expected_data = [
            {'id': 2, 'url': 'user', 'display': 'userLink'},
            {'id': 3, 'url': 'admin', 'display': 'adminLink'},
        ]
        assert response.json() == expected_data
