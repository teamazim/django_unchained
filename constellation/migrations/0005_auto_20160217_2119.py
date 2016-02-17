# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0004_auto_20160217_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
