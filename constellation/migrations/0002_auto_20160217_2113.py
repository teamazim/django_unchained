# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constellation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='addr_line_1',
            field=models.CharField(null=True, max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='addr_line_2',
            field=models.CharField(null=True, max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='signup',
            name='country',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='county',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='telephone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='signup',
            name='user',
            field=models.OneToOneField(default=datetime.datetime(2016, 2, 17, 21, 13, 35, 642337, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='last_name',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
    ]
