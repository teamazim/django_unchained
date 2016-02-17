# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0005_auto_20160217_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='age',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='telephone',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
    ]
