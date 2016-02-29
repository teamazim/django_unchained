from django.contrib import admin

# Register your models here.
from .models import UserProfiles, Events, Notes, Venues, Counties, Tickets, Bookings

admin.site.register(UserProfiles)
admin.site.register(Events)
admin.site.register(Notes)
admin.site.register(Venues)
admin.site.register(Counties)
admin.site.register(Tickets)
admin.site.register(Bookings)
