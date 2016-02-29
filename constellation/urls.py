"""
***Application url's***
"""

from django.conf.urls import url
from . import views

urlpatterns = [
	#localhost:8000/constellation
	url(r'^$', views.index, name='index'),	
	
	#localhost:8000/constellation/login 
	url(r'^login/$', views.Login, name='Login'),
	
	#localhost:8000/constellation/logout 
	url(r'^logout/$', views.Logout, name='Logout'),
	
	#localhost:8000/constellation/register
	url(r'^register/$', views.Register, name='Register'),
	
	#localhost:8000/constellation/munster
	url(r'^munster/$', views.Munster, name='Munster'),

	#localhost:8000/constellation/leinster
	url(r'^leinster/$', views.Leinster, name='Leinster'),

	#localhost:8000/constellation/connacht
	url(r'^connacht/$', views.Connacht, name='Connacht'),

	#localhost:8000/constellation/ulster
	url(r'^ulster/$', views.Ulster, name='Ulster'),

    #localhost:8000/constellation/?/checkin/
    url(r'^(?P<qr_code>[0-99999]+)/checkin/$', views.Checkin, name='Checkin'),
]