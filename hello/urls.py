from django.urls import path


from . import views


# Urls file for app named hello

# Named so that even if the routes change
# no need to change the template 
# refer to route by name
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]

