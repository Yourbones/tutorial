# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'click_nums', 'category', 'crate_time', 'modify_time')  # 博客相关字段展示

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)