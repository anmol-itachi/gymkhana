# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
        ('forum', '0011_remove_topic_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='total_votes',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AddField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oauth.UserProfile'),
            preserve_default=False,
        ),
    ]
