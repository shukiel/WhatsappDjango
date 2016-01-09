# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=1000)),
                ('time_sent', models.DateTimeField(verbose_name='TimeSent')),
                ('time_seen', models.DateTimeField(verbose_name='TimeSeen')),
            ],
        ),
        migrations.CreateModel(
            name='WhatsappUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='message_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Messaging.WhatsappUser'),
        ),
    ]
