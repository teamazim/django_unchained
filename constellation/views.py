"""
***Constellation views***
"""

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from .models import UserProfile
#index page / Landing page
def index(request):
	context = {
	}
	return render(request, 'constellation/landing_page.html', context)

#Sample home page?
def home(request):
	context = {
	'head_title': 'Constellation',
	}
	return render(request, 'constellation/home.html', context)

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

#First time user registration page
def Register(request):
	context = {
	}
	if request.method == 'POST':
		username = request.POST['id_username']
		email = request.POST['email']
		password = request.POST['pwd1']
		first_name = request.POST['first_name']
		last_name = request.POST['surname']
		age = request.POST['age']
		telephone = request.POST['telephone']
		addr_line_1 = request.POST['addr_line_1']
		addr_line_2 = request.POST['addr_line_2']
		county = request.POST['county']
		country = request.POST['country']
		
		user = User.objects.create_user(
		username = username,
		email = email,
		password = password
		)
		user.save()
		
		user_profile = UserProfile(
		user=user,
		first_name = first_name,
		last_name = last_name,
		age = age,
		telephone = telephone,
		addr_line_1 = addr_line_1,
		addr_line_2 = addr_line_2,
		county = county,
		country = country,
		)
		user_profile.save()
		user = authenticate(username=username, password=password)
		login(request, user)
		return render( request, 'constellation/home.html', context )
	else:
		return render( request, 'constellation/registration/signup.html', context )