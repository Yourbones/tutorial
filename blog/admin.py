# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Category, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'click_nums', 'category', 'create_time', 'modify_time')  # 博客相关字段展示
    list_per_page = 10                      # 设置每页显示多少条记录，默认是100条
    list_editable = ['category']            # 设置默认可编辑字段

admin.site.register(Category)
admin.site.register(Tag)