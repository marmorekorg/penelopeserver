# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 05:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 26, 5, 17, 34, 916694, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 4, 26, 5, 17, 39, 458609, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='twitter_date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 4, 26, 5, 17, 44, 130823, tzinfo=utc)),
            preserve_default=False,
        ),
    ]