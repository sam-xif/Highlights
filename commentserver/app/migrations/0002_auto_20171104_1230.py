# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-04 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='selectedText',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='webpage',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]