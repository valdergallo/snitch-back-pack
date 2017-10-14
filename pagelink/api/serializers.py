# coding=utf-8
from rest_framework import serializers
from pagelink.models import PageLink, PageLinkTracker


class PageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageLink
        fields = ('id', 'url', 'display')


class PageLinkTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageLinkTracker
        fields = ('page_link', 'user')

    def create(self, validated_data):
        return PageLinkTracker.objects.create(**validated_data)
