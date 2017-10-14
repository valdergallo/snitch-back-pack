# coding=utf-8
from rest_framework import viewsets
from pagelink.api.serializers import PageLinkSerializer
from pagelink.api.serializers import PageLinkTrackSerializer
from pagelink.models import PageLink
from pagelink.models import PageLinkTracker


class PageLinkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return the valid links for users
    """
    serializer_class = PageLinkSerializer
    queryset = PageLink.objects.none()
    http_method_names = ['get', 'post', 'head']

    def get_queryset(self):
        """
        This view should return a list of links
        for the currently authenticated user.
        """
        user = self.request.user
        return PageLink.objects.for_user(user=user)


class PageLinkTrackerViewSet(viewsets.ModelViewSet):
    """
    Save the link usage
    """
    serializer_class = PageLinkTrackSerializer
    queryset = PageLinkTracker.objects.all()
    http_method_names = ['get', 'post', 'head']
