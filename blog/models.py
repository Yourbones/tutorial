# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    title = models.CharField(u"博客标题", max_length = 100)
    tag = models.CharField(u"博客标签", max_length= 50,blank = True)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add = True,editable = True)
    update_time = models.DateTimeField(u"更新日期", auto_now = True, null=True)
    content = UEditorField(u"文章正文", height=300, width=770, default=u'', blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"


