# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_printful', '0010_auto_20170212_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfcatalogproduct',
            name='is_active',
            field=models.BooleanField(default=True, help_text='', verbose_name='Is Active?'),
        ),
        migrations.AlterField(
            model_name='pfcatalogsize',
            name='sort_order',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Sort Order'),
        ),
    ]