from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Atendee():
    user = models.OneToOneField(User),
    display_name = models.CharField(max_length=20),
    contact_number =  models.IntegerField(default=0),
    nationality = models.CharField(max_length=30),
    county = models.CharField(max_length=30),
    preferred_language = models.CharField(max_length=30),
    gender = models.CharField(max_length=15),
    on_delete = models.CASCADE,