# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20221122_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (4, '最近评论'), (3, '最热文章')], default=1, verbose_name='展示类型'),
        ),
    ]
