# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0006_auto_20160217_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
    ]
