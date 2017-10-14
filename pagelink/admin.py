from django.contrib import admin

# Register your models here.
from pagelink.models import PageLink


class PageLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'display')


admin.site.register(PageLink)
