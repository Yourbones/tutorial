# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import View
from blog.models import Blog, Tag, Category
from pure_pagination import PageNotAnInteger, Paginator
# Create your views here.

class IndexView(View):
    """
    首页
    """
    # GET请求
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 4, request=request)   # 5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'index.html',{
            'all_blog': all_blog,
        })

class ArchiveView(View):

    def get(self, request):
        all_blog = Blog.objects.all().order_by('-create_time')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 4, request=request)
        all_blog = p.page(page)

        return render(request, 'archive.html', {
            'all_blog': all_blog,
        })