# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_manufacturervariant_manufacturer'),
        ('api_gooten', '0008_auto_20161231_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='brand',
            new_name='c_brand',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='color',
            new_name='c_color',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='size',
            new_name='c_size',
        ),
        migrations.AddField(
            model_name='variant',
            name='c_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalog_item', to='catalog.Item'),
        ),
    ]