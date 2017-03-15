# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_auto_20170312_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pfprintfile',
            old_name='hash',
            new_name='phash',
        ),
        migrations.RenameField(
            model_name='pfprintfile',
            old_name='type',
            new_name='ptype',
        ),
        migrations.AddField(
            model_name='pfprintfile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='pfprintfile',
            name='preview_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Preview URL'),
        ),
    ]