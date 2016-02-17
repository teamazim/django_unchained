# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0003_auto_20160217_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 21, 17, 6, 320606, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 21, 17, 17, 176688, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
