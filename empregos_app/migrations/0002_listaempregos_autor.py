# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 15:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empregos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaempregos',
            name='autor',
            field=models.ForeignKey(max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]