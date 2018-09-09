# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from blog.models import Blog, Tag, Category, Comment, Counts
from blog.forms import  CommentForm
from pure_pagination import PageNotAnInteger, Paginator
import markdown


class IndexView(View):
    """
    首页
    """
    # GET请求
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # 博客、标签、分类数目统计
        try:
            count_nums = Counts.objects.get(id=1)
            blog_nums = count_nums.blog_nums
            category_nums = count_nums.category_nums
            tag_nums = count_nums.tag_nums
        except:
            blog_nums = 0
            category_nums = 0
            tag_nums = 0

        for blog in all_blog:
            blog.content = markdown.markdown(blog.content)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 4, request=request)   # 5为每页展示的博客数目
        all_blog = p.page(page)
        return render(request, 'index.html',{
            'all_blog': all_blog,
            'blog_nums': blog_nums,
            'cate_nums': category_nums,
            'tag_nums': tag_nums,
        })

class ArchiveView(View):

    def get(self, request):
        all_blog = Blog.objects.all().order_by('-create_time')
        counts = len(all_blog)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 4, request=request)
        all_blog = p.page(page)

        return render(request, 'archive.html', {
            'all_blog': all_blog,
            'counts': counts,
        })

class TagView(View):

    def get(self, request):
        all_tag = Tag.objects.all()
        counts = len(all_tag)
        return render(request, 'tags.html', {
            'all_tag': all_tag,
            'counts': counts,
        })

class TagDetailView(View):

    def get(self, request, tag_name):
        tag = Tag.objects.filter(name=tag_name).first()
        tag_blogs = tag.blog_set.all()
        counts = len(tag_blogs)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 3, request=request)
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html',{
            'tag_blogs': tag_blogs,
            'tag_name': tag_name,
        })

class BlogDetailView(View):
    """
    博客详情页
    """
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        all_comment = Comment.objects.filter(blog=blog)
        # 将博客内容用markdown显示出来
        blog.content = markdown.markdown(blog.content)

        has_prev = False
        has_next = False
        id_prev = id_next = int(blog_id)                          # 初始化变量
        blog_id_max = Blog.objects.all().order_by('-id').first()  # 通过筛选获得最后一个数据的id
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first() # 假设博客删除，则前面id不存在
            if not blog_prev:
                id_prev -= 1
            else:
                has_prev = True
        while not has_next and id_next <= id_max:
            blog_next = Blog.objects.filter(id=id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True
        return render(request, 'blog-detail.html', {
            'blog': blog,
            'blog_prev': blog_prev,
            'blog_next': blog_next,
            'has_prev': has_prev,
            'has_next': has_next,
            'all_comment': all_comment,
        })

# 通过json来向前端传递参数，并通过Ajax异步的方式进行评论
class AddCommentView(View):

    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')


class CategoryDetailView(View):

    def get(self, request, category_name):
        category = Category.objects.filter(name=category_name).first()
        cate_blogs  = category.blog_set.all()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(cate_blogs, 5, request=request)
        cate_blogs = p.page(page)

        return render(request, 'category-detail.html', {
            'cate_blogs': cate_blogs,
            'category_name': category_name,
        })


