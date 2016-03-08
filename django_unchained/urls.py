"""
***Project urls***
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	#localhost:8000/constellation 
	url(r'^constellation/', include('constellation.urls')),
	
	url(r'^grappelli/', include('grappelli.urls')),

	#localhost:8000/admin
	url(r'^admin/', include(admin.site.urls)),

	url(r'^', 'constellation.views.index'),

]
