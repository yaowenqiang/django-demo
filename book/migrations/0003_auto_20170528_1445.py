# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20170528_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
