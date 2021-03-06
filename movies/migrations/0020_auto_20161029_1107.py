# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20161029_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='key_actors',
            field=models.ManyToManyField(blank=True, related_name='acted_movies', to='movies.Person', verbose_name='list of key actors'),
        ),
    ]
