from django.contrib import admin

# Register your models here.
from .models import UserProfile, UserProfiles, Events, Notes, Venues, Counties, Bookings

admin.site.register(UserProfile)
admin.site.register(UserProfiles)
admin.site.register(Events)
admin.site.register(Notes)
admin.site.register(Venues)
admin.site.register(Counties)
admin.site.register(Bookings)
