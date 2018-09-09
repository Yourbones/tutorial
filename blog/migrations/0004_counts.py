# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-09 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_nums', models.IntegerField(default=0, verbose_name='博客数目')),
                ('category_nums', models.IntegerField(default=0, verbose_name='分类数目')),
                ('tag_nums', models.IntegerField(default=0, verbose_name='标签数目')),
                ('visit_nums', models.IntegerField(default=0, verbose_name='网站访问量')),
            ],
            options={
                'verbose_name': '数目统计',
                'verbose_name_plural': '数目统计',
            },
        ),
    ]
