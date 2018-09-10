# -*- coding:utf-8 -*-
"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from Myblog.settings import STATIC_ROOT
from django.conf import settings
from blog.views import IndexView, ArchiveView, TagView,\
    TagDetailView, BlogDetailView, AddCommentView, CategoryDetailView, page_not_found, page_errors


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^archive/$',ArchiveView.as_view(), name='archive'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)$',TagDetailView.as_view(), name='tag_name'),
    url(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^category/(?P<category_name>\w+)/$', CategoryDetailView.as_view(), name='category_name'),
    url(r'^static/(?P<path>.*)/$', 'django.views.static.serve',{'document_root': STATIC_ROOT}),
]
hander404 = 'blog.views.page_not_found'
hander505 = 'blog.views.page_errors'