from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "hello/index.html", context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")

    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # exclude to exclude that satisfies ,
        # filter means include those that satisfy.
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }

    return render(request, "hello/flight.html", context)


def book(request, flight_id):
    print("Flight id is", flight_id)
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except Passenger.DoesNotExist:
        return render(request, "hello/error.html", {"message": "No passenger"})
    except Flight.DoesNotExist:
        return render(request, "hello/error.html", {"message": "No flight"})
    except KeyError:
        return render(request, "hello/error.html", {"message": "No selection"})

    passenger.flights.add(flight)

    # getting url from name of route is called reverse
    # the , is important as else it's just a int while with , it is tuple
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))