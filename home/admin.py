from django.contrib import admin
from home.models import Bookings, Contact, CricketTiming

# Register your models here.
admin.site.register(Contact)
admin.site.register(Bookings)
admin.site.register(CricketTiming)