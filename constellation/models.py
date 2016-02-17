from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# email = models.EmailField()
	first_name = models.CharField( max_length=40 )
	last_name = models.CharField( max_length=40 )
	# age = models.CharField( max_length=40 )
	# telephone = models.CharField( max_length=40 )
	# addr_line_1 = models.CharField( max_length=120 )
	# addr_line_2 = models.CharField( max_length=120 )
	# county = models.CharField( max_length=40 )
	# country = models.CharField( max_length=40 )

User.profile = property( lambda u: UserProfile.objects.get_or_create(user=u)[0])