# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^maps/', include('maps.urls')),

)
