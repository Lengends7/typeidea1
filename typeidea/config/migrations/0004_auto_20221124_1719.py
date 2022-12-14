# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-24 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20221124_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, '隐藏'), (1, '展示')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(2, '最新文章'), (1, 'HTML'), (4, '最近评论'), (3, '最热文章')], default=1, verbose_name='展示类型'),
        ),
    ]
