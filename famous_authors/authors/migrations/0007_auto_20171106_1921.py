# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_auto_20171106_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
