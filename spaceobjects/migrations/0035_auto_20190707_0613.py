# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-07 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceobjects', '0034_shapemodel_source'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='spaceobject',
            index=models.Index(fields=['a'], name='spaceobject_a_f9bd0b_idx'),
        ),
    ]