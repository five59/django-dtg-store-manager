# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0019_auto_20170214_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bzproduct',
            name='code',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Code'),
        ),
    ]
