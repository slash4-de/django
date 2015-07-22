"""myevent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'events.views.home', name='home'),
    url(r'^events/$', 'events.views.list', name='event_list'),
    url(r'^events/(?P<id>\d+)/$', 'events.views.detail', name='event_detail'),

    url(r'^register/$', 'events.views.register', name='register'),
    url(r'^login/$', auth_view.login, name='login', kwargs={'template_name': 'users/login.html'}),
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^events/join/(?P<event_id>\d+)/$', 'events.views.join', name='event_join'),
]
