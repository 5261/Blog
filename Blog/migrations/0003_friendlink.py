# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20160804_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
                ('link', models.URLField(verbose_name='Link')),
            ],
        ),
    ]
