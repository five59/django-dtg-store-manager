# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20161111_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Code'),
        ),
    ]