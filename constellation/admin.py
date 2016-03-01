from django.contrib import admin

# Register your models here.
from .models import UserProfile, UserProfiles, Event, Note, Venue, County, Booking

admin.site.register(UserProfile)
admin.site.register(UserProfiles)
admin.site.register(Event)
admin.site.register(Note)
admin.site.register(Venue)
admin.site.register(County)
admin.site.register(Booking)
