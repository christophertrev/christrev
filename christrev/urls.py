from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include('startpage.urls', namespace='startpage', app_name='startpage')),
    url(r'^about/', views.index, name='about'),

    url(r'^$', views.cover, name='cover'),

)
