# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('room_id', models.CharField(max_length=6)),
                ('native_sender', models.BooleanField()),
                ('message_content', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('message_status', models.IntegerField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MessageRoom',
            fields=[
                ('room_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('native', models.CharField(max_length=6, null=True)),
                ('learner', models.CharField(max_length=6, null=True)),
            ],
        ),
    ]
