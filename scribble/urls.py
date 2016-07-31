"""wildblogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from scribbleapp.views import *

from django.conf.urls import url
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home, name='home'),
     url(r'^post/new$', add_post),
    url(r'^post/view$', all_posts, name="view_post"),
    url(r'^post/view_post/(?P<slug>[-\w]+)$', view_post),
    url(r'^post/delete/(?P<pk>[0-9]+)$', PostDelete.as_view(), name='view_post'),
    url(r'^post/update/(?P<pk>[0-9]+)$', PostUpdate.as_view(), name='view_post'),
    url(r'^about', about),
    url(r'^viewall', view_all_posts),
    url(r'^viewpost/(?P<slug>[-\w]+)$', view_other_post),
)
