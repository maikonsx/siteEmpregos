# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empregos_app', '0010_auto_20180422_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listaempresas',
            name='nomeEmprego',
        ),
        migrations.AddField(
            model_name='listaempresas',
            name='nomeEmprego',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empregos_app.listaEmpregos'),
            preserve_default=False,
        ),
    ]
