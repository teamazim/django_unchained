"""
***Constellation views***
"""

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import datetime

# index page
def index(request):
	queryset = UserProfile.objects.all()
	context = {
	'head_title': 'Constellation',
	'object_list': queryset
	}
	return render(request, 'constellation/home.html', context)


# Logout a user / End session
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/constellation')


# Login a user / Starts session
def Login(request):
    next = request.GET.get('next', '/constellation')
    if request.method == "POST":  # when submit button is pressed
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
    return render(request, 'constellation/login.html', {'redirect_to': next})  # Initial view


# First time user registration page
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
                username=username,
                email=email,
                password=password
        )
        user.save()  # Create and save user

        user_profile = UserProfile(
                user=user,
                first_name=first_name,
                last_name=last_name,
                age=age,
                telephone=telephone,
                addr_line_1=addr_line_1,
                addr_line_2=addr_line_2,
                county=county,
                country=country,
        )
        user_profile.save()  # create and save user profile

        user = authenticate(username=username, password=password)  # start a session
        login(request, user)
        return render(request, 'constellation/home.html', context)  # redirect to homepage
    else:
        return render(request, 'constellation/registration/signup.html', context)


# Munster page
def Munster(request):
    context = {
        'head_title': 'Constellation',
    }
    return render(request, 'constellation/munster.html', context)


# Leinster page
def Leinster(request):
    context = {
        'head_title': 'Constellation',
    }
    return render(request, 'constellation/leinster.html', context)


# Ulster page
def Ulster(request):
    context = {
        'head_title': 'Constellation',
    }
    return render(request, 'constellation/ulster.html', context)


# Connacht page
def Connacht(request):
    context = {
        'head_title': 'Constellation',
    }
    return render(request, 'constellation/connacht.html', context)


def Checkin(request, qr_code):
    if Bookings.objects.filter(qrCode = qr_code).exists():
        bookingObject = Bookings.objects.get(qrCode = qr_code)
        userProfileObject = UserProfiles.objects.get(userID = bookingObject.userID)
        if bookingObject.confirmed == False:
            now = datetime.datetime.now()
            html = "<html><head>Checked-In</head><body><p>%s &s %s Checked in at %s.</body></html>" % (userProfileObject.first_name, userProfileObject.last_name, now)
            return HttpResponse(html)
        else:

            html = "<html><head>Already Checked-In</head><body><p>%s &s %s Checked in at %s %s.</body></html>" % (userProfileObject.first_name, userProfileObject.last_name, bookingObject.checkinTime, bookingObject.checkinDate)
            return HttpResponse(html)
    else:
        html = "<html><head>Invalid QR Code</head><body><p>%s does not match any booking.</body></html>" % qr_code
        return HttpResponse(html)
