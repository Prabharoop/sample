from django.contrib import admin

from .models import Flight, Airport, Passenger


# Modify admin interface
class PassengerInline(admin.StackedInline):
    # through is the way to access the intermediary
    # table between flights and passengers

    # This modification is done to allow the 
    # flight class to add new passengers
    # like the passenger can add flights
    model = Passenger.flights.through
    #One additonal passenger at a time
    extra = 1

# Add additonal inline section to flight admin settings
class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]


# Additonal info about how I want 
# the users of the admin page to interact with
# the passenger model
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)

