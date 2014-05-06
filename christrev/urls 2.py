from django.conf.urls import patterns, include, url

from startpage import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^about/', views.index, name='about'),

    url(r'^$', views.cover, name='cover'),




)
