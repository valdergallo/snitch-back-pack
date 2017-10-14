# coding=utf-8
from django.test import TestCase
from pagelink.tests.fixtures import (
    create_default_links_and_users, USER_PASSWORD)
from rest_framework.test import APIClient
from django.urls import reverse
from pagelink.models import PageLink
from pagelink.models import PageLinkTracker


class TestPageLinkTrackerViewSetSaveItem(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls = create_default_links_and_users(cls)

    def setUp(self):
        self.client = APIClient()

    def test_record_one_track(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )

        post_data = {
            'user': self.user.id,
            'page_link': PageLink.objects.first().id,
        }

        assert PageLinkTracker.objects.count() == 0

        response = self.client.post(
            reverse('pagelinktracker-list'), post_data)

        assert response.status_code == 201  # Success

        assert PageLinkTracker.objects.count() == 1

    def test_denied_update_tracker_with_post(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )

        post_data = {
            'user': self.user.id,
            'page_link': PageLink.objects.first().id,
        }

        self.client.post(
            reverse('pagelinktracker-list'), post_data)

        first = PageLinkTracker.objects.first()

        # try update last record
        response = self.client.post(
            reverse('pagelinktracker-detail', args=[first.id]), post_data)

        assert response.status_code == 405  # Not Allowed

    def test_denied_update_tracker(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )

        post_data = {
            'user': self.user.id,
            'page_link': PageLink.objects.first().id,
        }

        self.client.post(
            reverse('pagelinktracker-list'), post_data)

        first = PageLinkTracker.objects.first()

        # try update last record
        response = self.client.put(
            reverse('pagelinktracker-detail', args=[first.id]), post_data)

        assert response.status_code == 405  # Not Allowed

    def test_denied_delete_tracker(self):
        self.client.login(
            username=self.user.username,
            password=USER_PASSWORD
        )

        post_data = {
            'user': self.user.id,
            'page_link': PageLink.objects.first().id,
        }

        self.client.post(
            reverse('pagelinktracker-list'), post_data)

        first = PageLinkTracker.objects.first()

        # try update last record
        response = self.client.delete(
            reverse('pagelinktracker-detail', args=[first.id]), post_data)

        assert response.status_code == 405  # Not Allowed

    def test_register_tracker_with_token(self):
        data = {
            'username': self.admin_user.username, 
            'password': USER_PASSWORD
        }
        token = self.client.post('/api-token/', data, follow=True)

        assert token.status_code == 200
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        assert token.data['id'] == self.admin_user.id

        post_data = {
            'user': self.admin_user.id,
            'page_link': PageLink.objects.first().id,
        }

        self.client.post(
            reverse('pagelinktracker-list'), post_data)

        assert PageLinkTracker.objects.count() == 1