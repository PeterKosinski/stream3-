# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:38
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0014_school_business_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Business_des',
            field=tinymce.models.HTMLField(default='-'),
        ),
    ]
