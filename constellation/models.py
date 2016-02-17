from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class SignUp(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField()
	first_name = models.CharField( max_length=40, null=True, blank=True )
	last_name = models.CharField( max_length=40, null=True, blank=True )
	age = models.CharField( max_length=40, null=True, blank=True )
	telephone = models.CharField( max_length=40, null=True, blank=True )
	addr_line_1 = models.CharField( max_length=120, null=True, blank=True )
	addr_line_2 = models.CharField( max_length=120, null=True, blank=True )
	county = models.CharField( max_length=40, null=True, blank=True )
	country = models.CharField( max_length=40, null=True, blank=True )