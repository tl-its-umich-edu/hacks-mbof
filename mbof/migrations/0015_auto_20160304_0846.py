# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mbof.models


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0014_auto_20160304_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(default='bjensen', on_delete=django.db.models.deletion.CASCADE, to='mbof.User'),
        ),
    ]
