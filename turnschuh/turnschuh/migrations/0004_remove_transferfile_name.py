# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-16 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnschuh', '0003_auto_20191016_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferfile',
            name='name',
        ),
    ]