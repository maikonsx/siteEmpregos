# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregos_app', '0003_auto_20180422_1927'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tipoEmpregos',
        ),
        migrations.AlterField(
            model_name='listaempregos',
            name='titulo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
