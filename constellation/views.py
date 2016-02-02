"""
***Constellation views***
"""

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

#index page / Landing page
def index(request):
	context = {
	'head_title': 'Constellation',
	}
	return render(request, 'constellation/landing_page.html', context)

#Sample home page?
def home(request):
	context = {
	'head_title': 'Constellation',
	}
	return render(request, 'constellation/base.html', context)

#Logout a user / End session 
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/constellation')

#Login a user / Starts session
def Login(request):
	next = request.GET.get('next', '/constellation')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse('Inactive user.')
		else:
			return HttpResponseRedirect('')
	return render( request, 'constellation/login.html', {'redirect_to' : next} )