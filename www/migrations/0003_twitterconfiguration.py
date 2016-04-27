# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20160426_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_key', models.CharField(max_length=200)),
                ('consumer_secret', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('access_token_secret', models.CharField(max_length=200)),
            ],
        ),
    ]