# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 16:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], default='M', max_length=1)),
                ('roll', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('enroll_year', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^[0-9]{4}$', message='Not a valid year!')])),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', message='Not a valid number!')])),
                ('avatar', models.ImageField(upload_to='avatar')),
                ('hometown', models.CharField(max_length=128)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=5)),
                ('about', models.CharField(max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
