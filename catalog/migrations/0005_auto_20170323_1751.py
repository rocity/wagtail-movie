# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_moviepagegalleryimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoviePageGalleryImage',
            new_name='MoviePageMovieImage',
        ),
    ]