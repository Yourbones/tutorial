# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-09 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180908_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='佚名', max_length=20, verbose_name='姓名')),
                ('content', models.CharField(max_length=300, verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='博客')),
            ],
            options={
                'verbose_name': '博客评论',
                'verbose_name_plural': '博客评论',
            },
        ),
    ]