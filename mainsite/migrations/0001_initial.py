# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-24 08:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2017, 5, 24, 8, 18, 38, 381000, tzinfo=utc))),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
