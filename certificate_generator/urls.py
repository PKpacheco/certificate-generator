# coding: utf-8

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include('api.urls')),
    # url(r'^', include('homesite.urls', namespace='homesite')),
    # url(r'^categories/', include('categories.urls', namespace='categories')),
    # url(r'^convites/', include('invites.urls', namespace='convites')),
    url(r'^pdf/', include('certificate.urls', namespace='pdf')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
