# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils import timezone

class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='文章类别', max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    博客
    """
    title = models.CharField(verbose_name="博客标题", max_length = 100)
    tag = models.ManyToManyField(Tag, verbose_name="文章标签")
    category = models.ForeignKey(Category, verbose_name="文章类别")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add = True,editable=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    click_nums = models.IntegerField(verbose_name="点击量", default=0)
    content = UEditorField(verbose_name="文章正文", height=300, width=770, default=u'', blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = "我的博客"
        verbose_name_plural = verbose_name


