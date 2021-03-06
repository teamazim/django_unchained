# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 00:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('eventID', models.IntegerField()),
                ('qrCode', models.CharField(blank=True, max_length=20, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('checkinTime', models.TimeField(blank=True, null=True)),
                ('checkinDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('countyID', models.AutoField(primary_key=True, serialize=False)),
                ('countyName', models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], max_length=9)),
                ('province', models.CharField(choices=[('connacht', 'Connacht'), ('leinster', 'Leinster'), ('munster', 'Munster'), ('ulster', 'Ulster')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('eventDescription', models.TextField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('venueID', models.IntegerField()),
                ('season', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')], max_length=6)),
                ('notesID', models.IntegerField(blank=True, null=True)),
                ('availability', models.IntegerField(blank=True, null=True)),
                ('youtubeVideoID', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('notesID', models.AutoField(primary_key=True, serialize=False)),
                ('fileName', models.CharField(max_length=50)),
                ('dataType', models.CharField(max_length=10)),
                ('noteDescription', models.TextField()),
                ('dateAdded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='test', max_length=40)),
                ('last_name', models.CharField(default='test', max_length=40)),
                ('age', models.CharField(default='test', max_length=40)),
                ('telephone', models.CharField(default='test', max_length=40)),
                ('addr_line_1', models.CharField(default='test', max_length=120)),
                ('addr_line_2', models.CharField(default='test', max_length=120)),
                ('county', models.CharField(default='test', max_length=40)),
                ('country', models.CharField(default='test', max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('userAddress', models.TextField()),
                ('userCounty', models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], max_length=9)),
                ('userCountry', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('language', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venueID', models.AutoField(primary_key=True, serialize=False)),
                ('venueName', models.CharField(max_length=50)),
                ('venueAddress', models.TextField()),
                ('venueCounty', models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], max_length=9)),
                ('venueCountry', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('venueType', models.CharField(choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor')], max_length=7)),
            ],
        ),
    ]
