# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-24 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221122_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveIntegerField(choices=[(2, '草稿'), (0, '删除'), (1, '正常')], verbose_name='状态'),
        ),
    ]