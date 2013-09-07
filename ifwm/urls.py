#! /usr/bin/env python2.7
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from ifwm.home.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^page(?P<id>[0-9]*)$', ImagesPageView.as_view()),
    url(r'^add$', AddUrlView.as_view()),
    url(r'^progress$', PageProgress),
    # static
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve,
        {'show_indexes': True, 'insecure': False}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
)
