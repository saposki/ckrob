# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-10 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160210_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]