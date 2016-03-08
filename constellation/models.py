from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_ID = models.AutoField(primary_key=True)
	first_name = models.CharField( max_length=40, default='test')
	last_name = models.CharField( max_length=40, default='test' )
	age = models.CharField( max_length=40, default='test' )
	telephone = models.CharField( max_length=40, default='test' )
	addr_line_1 = models.CharField( max_length=120, default='test' )
	addr_line_2 = models.CharField( max_length=120, default='test' )
	county = models.CharField( max_length=40, default='test' )
	country = models.CharField( max_length=40, default='test' )

	def __str__(self):              # __unicode__ on Python 2
		return self.first_name

COUNTIES = (
    ('Antrim', 'Antrim'),
    ('Armagh', 'Armagh'),
    ('Carlow', 'Carlow'),
    ('Cavan', 'Cavan'),
    ('Clare', 'Clare'),
    ('Cork', 'Cork'),
    ('Derry', 'Derry'),
    ('Donegal', 'Donegal'),
    ('Down', 'Down'),
    ('Dublin', 'Dublin'),
    ('Fermanagh', 'Fermanagh'),
    ('Galway', 'Galway'),
    ('Kerry', 'Kerry'),
    ('Kildare', 'Kildare'),
    ('Kilkenny', 'Kilkenny'),
    ('Laois', 'Laois'),
    ('Leitrim', 'Leitrim'),
    ('Limerick', 'Limerick'),
    ('Longford', 'Longford'),
    ('Louth', 'Louth'),
    ('Mayo', 'Mayo'),
    ('Meath', 'Meath'),
    ('Monaghan', 'Monaghan'),
    ('Offaly', 'Offaly'),
    ('Roscommon', 'Roscommon'),
    ('Sligo', 'Sligo'),
    ('Tipperary', 'Tipperary'),
    ('Tyrone', 'Tyrone'),
    ('Waterford', 'Waterford'),
    ('Westmeath', 'Westmeath'),
    ('Wexford', 'Wexford'),
    ('Wicklow', 'Wicklow'),
)

class UserProfiles(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.AutoField(primary_key=True)
    dob = models.DateField()
    userAddress = models.TextField()
    userCounty = models.CharField(max_length = 9, choices=COUNTIES)
    userCountry = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    language = models.CharField(max_length = 50)

class Event(models.Model):
	SEASONS = (
	('spring', 'Spring'),
	('summer', 'Summer'),
	('autumn', 'Autumn'),
	('winter', 'Winter'),
	)
	eventID = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 50)
	eventDescription = models.TextField()
	startTime = models.TimeField()
	endTime = models.TimeField()
	startDate = models.DateField()
	endDate = models.DateField()
	venueID = models.IntegerField()
	season = models.CharField(max_length=6, choices=SEASONS)
	notesID = models.IntegerField(null=True, blank=True)
	availability = models.IntegerField(null=True, blank=True)
	youtubeVideoID = models.CharField(max_length=20, blank=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.title

class Note(models.Model):
    notesID = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length = 50)
    dataType = models.CharField(max_length = 10)
    noteDescription = models.TextField()
    dateAdded = models.DateField()

class Venue(models.Model):
	VENUE_TYPES = (
		('indoor', 'Indoor'),
		('outdoor', 'Outdoor'),
	)
	venueID = models.AutoField(primary_key=True)
	venueName = models.CharField(max_length = 50)
	venueAddress = models.TextField()
	venueCounty = models.CharField(max_length = 9, choices=COUNTIES)
	venueCountry = models.CharField(max_length = 50)
	capacity = models.PositiveIntegerField()
	venueType = models.CharField(max_length=7, choices=VENUE_TYPES)

	def __str__(self):              # __unicode__ on Python 2
		return self.venueName


class County(models.Model):
	PROVINCES = (
		('connacht', 'Connacht'),
		('leinster', 'Leinster'),
		('munster', 'Munster'),
		('ulster', 'Ulster'),
	)
	countyID = models.AutoField(primary_key=True)
	countyName = models.CharField(max_length=9, choices=COUNTIES)
	province = models.CharField(max_length=8, choices=PROVINCES)

	def __str__(self):              # __unicode__ on Python 2
		return self.countyName


class Booking(models.Model):
    bookingID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    eventID = models.IntegerField()
    qrCode = models.CharField(max_length = 20, null=True, blank=True)
    confirmed = models.BooleanField(default = False)
    checkinTime = models.TimeField(null=True, blank=True)
    checkinDate = models.DateField(null=True, blank=True)

