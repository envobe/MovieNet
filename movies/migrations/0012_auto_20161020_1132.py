# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20161020_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name'], 'verbose_name_plural': 'people'},
        ),
    ]
