# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_school_rsa_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]