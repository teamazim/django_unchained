from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=120, null=True, blank=True )
    last_name = models.CharField( max_length=120, null=True, blank=True )
    email = models.EmailField()
    timestamp = models.DateTimeField( auto_now_add=True, auto_now=False )
    updated = models.DateTimeField( auto_now_add=False, auto_now=True )