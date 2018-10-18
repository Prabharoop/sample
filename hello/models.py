from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} - {self.city}"


class Flight(models.Model):
    # models.CASCADE to delete all flights once the 
    # airport that it corresponds to is deleted.

    # related_name can be used to identify all the flights 
    # that correspond to a particular Airport.
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def is_valid_flight(self):
        return (self.origin != self.destination and (self.duration >= 0))

    def __str__(self):
        return f"{self.id}- {self.origin} - {self.duration}"



#MANY TO MANY MODEL For flights and passenegers

#p.flights.add(f) where p is passenger and f is flight

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

  
#from flights.models import Flight
# f = Flight(origin=, destination=, duration=)
# f.save()
# f.delete()
# Flight.objects.all()

# >>> from hello.models import Airport, Flight
# >>> jfk = Airport(code ="JFK", city="New York City")
# >>> lhr = Airport(code="LHR", city="London")
# >>> 
# >>> jfk.save()
# >>> lhr.save()
# >>> 
# >>> f = Flight(origin=jfk, destination=lhr, duration=415)
# >>> f.save()
