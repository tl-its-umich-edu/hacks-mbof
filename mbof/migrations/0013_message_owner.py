# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0012_remove_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(default='bjensen', on_delete=django.db.models.deletion.CASCADE, to='mbof.User'),
            preserve_default=False,
        ),
    ]