# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constellation', '0007_auto_20160217_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(null=True, max_length=40, blank=True)),
                ('last_name', models.CharField(null=True, max_length=40, blank=True)),
                ('age', models.CharField(null=True, max_length=40, blank=True)),
                ('telephone', models.CharField(null=True, max_length=40, blank=True)),
                ('addr_line_1', models.CharField(null=True, max_length=120, blank=True)),
                ('addr_line_2', models.CharField(null=True, max_length=120, blank=True)),
                ('county', models.CharField(null=True, max_length=40, blank=True)),
                ('country', models.CharField(null=True, max_length=40, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
