# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huts', '0005_auto_20170503_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
