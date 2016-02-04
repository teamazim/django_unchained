"""
***Application url's***
"""

from django.conf.urls import url
from . import views

urlpatterns = [
	#localhost:8000/constellation
	url(r'^$', views.index, name='index'),
	
	#localhost:8000/constellation/home
	url(r'^home/$', views.home, name='home'),
	
	#localhost:8000/constellation/login 
	url(r'^login/$', views.Login, name='Login'),
	
	#localhost:8000/constellation/logout 
	url(r'^logout/$', views.Logout, name='Logout'),
	
	#localhost:8000/constellation/register
	url(r'^register/$', views.Register, name='Register'),
]