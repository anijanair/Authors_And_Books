# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20171106_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, default=''),
        ),
    ]
