from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField( max_length=40, default='test')
	last_name = models.CharField( max_length=40, default='test' )
	age = models.CharField( max_length=40, default='test' )
	telephone = models.CharField( max_length=40, default='test' )
	addr_line_1 = models.CharField( max_length=120, default='test' )
	addr_line_2 = models.CharField( max_length=120, default='test' )
	county = models.CharField( max_length=40, default='test' )
	country = models.CharField( max_length=40, default='test' )