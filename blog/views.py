# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,Http404
from blog.models import Article
from datetime import datetime

def home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/home.html', {'post_list': post_list})

def Test(request):
    return render(request, 'blog/test.html', {'current_time': datetime.now()})

def Detail(request,id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html', {'post': post})
