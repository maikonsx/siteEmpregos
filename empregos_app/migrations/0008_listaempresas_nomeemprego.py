# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregos_app', '0007_listaempresas'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaempresas',
            name='nomeEmprego',
            field=models.ManyToManyField(to='empregos_app.listaEmpregos'),
        ),
    ]
