"""
***Constellation views***
"""

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import datetime


# index page
def index(request):
	past = Event.objects.get(season = 'spring')
	present = Event.objects.get(season = 'summer')
	future = Event.objects.get(season = 'winter')
	user = request.user.id
	if user is not None:
		profile = UserProfile.objects.get(user=user)
		context = {
		'head_title': 'Constellation',
		'profile': profile,
		'past': past,
		'present': present,
		'future': future,
		}
	else:
		context = {
		'head_title': 'Constellation',
		'past': past,
		'present': present,
		'future': future,
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
	event = Event.objects.get(eventID=1)
	venue = Venue.objects.get( venueID = event.venueID )
	context = {
	'head_title': 'Constellation',
	'event': event,
	'venue': venue,
	}
	return render(request, 'constellation/munster.html', context)


# Leinster page
def Leinster(request):
	event = Event.objects.get(eventID=2)
	venue = Venue.objects.get( venueID = event.venueID )
	context = {
	'head_title': 'Constellation',
	'event': event,
	'venue': venue,
	}
	return render(request, 'constellation/leinster.html', context)


# Ulster page
def Ulster(request):
	event = Event.objects.get(eventID=4)
	venue = Venue.objects.get( venueID = event.venueID )
	context = {
	'head_title': 'Constellation',
	'event': event,
	'venue': venue,
	}
	return render(request, 'constellation/ulster.html', context)


# Connacht page
def Connacht(request):
	event = Event.objects.get(eventID=3)
	venue = Venue.objects.get( venueID = event.venueID )
	context = {
	'head_title': 'Constellation',
	'event': event,
	'venue': venue,
	}
	return render(request, 'constellation/connacht.html', context)


#Checkin page where a scanned qr code takes you to validate that particular code
def Checkin(request, qr_code):
    if Booking.objects.filter(qrCode = qr_code).exists():
        now = datetime.datetime.now().replace(microsecond=0)
        bookingObject = Booking.objects.get(qrCode = qr_code)
        userProfileObject = UserProfile.objects.get(id = bookingObject.userID)
        eventObject = Event.objects.get(eventID = bookingObject.eventID)
        if eventObject.startDate == now:
            if bookingObject.confirmed == False:
                bookingObject.confirmed = True
                bookingObject.checkinDate = now
                bookingObject.checkinTime = now
                bookingObject.save()
                html = "<html><head>Checked-In</head><body><p>%s %s Checked in at %s.</body></html>" % (userProfileObject.first_name, userProfileObject.last_name, now)
                return HttpResponse(html)
            else:
                html = "<html><head>Already Checked-In</head><body><p>%s %s Checked in at %s.</body></html>" % (userProfileObject.first_name, userProfileObject.last_name, bookingObject.checkinTime)
                return HttpResponse(html)
        else:
            html = "<html><head>The event \"%s\" hasn't started yet.</head><body><p>Please check in when the event starts on %s.</body></html>" % (eventObject.title, eventObject.startDate)
            return HttpResponse(html)
    else:
        html = "<html><head>Invalid QR Code</head><body><p>%s does not match any booking.</body></html>" % qr_code
        return HttpResponse(html)


#AT THE MOMENT MISSING HOW TO GET THE CURRENT BOOKING ID AND ALSO A PATH TO THE HTML TEMPLATE
#Generates a ticket from a particular booking ID
def GenerateTicket(request):
	bookingObject = Booking.objects.get(bookingID = 1)

	userProfileObject = UserProfile.objects.get(user_ID = bookingObject.userID)
	eventObject = Event.objects.get(eventID = bookingObject.eventID)
	venueObject = Venue.objects.get(venueID =  eventObject.venueID)

	HTML_MESSAGE = loader.render_to_string(
	'../templates/constellation/ticket.html',
	{
	"event_title": eventObject.title,
	"event_description": eventObject.eventDescription,
	"first_name": userProfileObject.first_name,
	"last_name": userProfileObject.last_name,
	"start_time": eventObject.startTime,
	"start_date": eventObject.startDate,
	"venue_name": venueObject.venueName,
	"venue_address": venueObject.venueAddress,
	"venue_county": venueObject.venueCounty,
	"qr_code": bookingObject.qrCode
	}
	)

	SUBJECT = "Your ticket for " + eventObject.title
	MESSAGE = ""
	FROM_EMAIL = settings.EMAIL_HOST_USER
	TO_EMAIL = ["teamazim829@gmail.com"]
	FAIL_SILENTLY = True
	send_mail(SUBJECT, MESSAGE, FROM_EMAIL, TO_EMAIL, fail_silently = FAIL_SILENTLY, html_message = HTML_MESSAGE)

	user = request.user.id
	if user is not None:
		profile = UserProfile.objects.get(user=user)
		context = {
		'profile': profile,
		'event': eventObject,
		'venue': venueObject,
		}
	else:
		context = {
		'head_title': 'Constellation',
		'event': eventObject,
		'venue': venueObject,
		}
	return render(request, 'constellation/success.html', context)

#AT THE MOMENT THIS JUST RETURNS THE NAME OF THE PROVINCE BUT COULD LEAD TO PAGE OF ALL EVENTS
#Ticket page where a ticket booking is made and a call to generate a ticket is made
def GetTicket(request, province):
    if province not in ["munster", "leinster", "connacht", "ulster"]:
        return HttpResponse("Error. Not valid province")
    else:
        #newBooking = Booking(userID = CURRENT, eventID = CURRENT)
        #newBooking.qrCode = str(newBooking.bookingID) + str(newBooking.userID) + str(newBooking.eventID)
        #newBooking.save()
        #Call generate ticket method passing through the booking ID
        return HttpResponse(province)