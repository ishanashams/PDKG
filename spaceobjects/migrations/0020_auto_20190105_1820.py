# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-05 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceobjects', '0019_auto_20190105_1818'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='orbitclass',
            index=models.Index(fields=['slug'], name='spaceobject_slug_610d6e_idx'),
        ),
        migrations.AddIndex(
            model_name='orbitclass',
            index=models.Index(fields=['abbrev'], name='spaceobject_abbrev_697070_idx'),
        ),
    ]