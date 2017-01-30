# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20170128_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='native_sender',
        ),
        migrations.AddField(
            model_name='message',
            name='message_sender',
            field=models.CharField(default='nothing', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
