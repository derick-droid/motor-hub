from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from cars.models import Car

# to display a home page
def home(request):
    # fetching data from data to the home view
    teams = Team.objects.all() # this fetches all the data from Team model
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured = True)
    all_cars = Car.objects.order_by("-created_date")
    # search_fields = Car.objects.values("model", "year", "body_style")
    model_search = Car.objects.values_list("model", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    body_search = Car.objects.values_list("body_style", flat=True).distinct()
    
    data = {
        'teams': teams,
        'featured_cars' : featured_cars,
        'all_cars': all_cars,
        # 'search_fields' : search_fields,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_search' : body_search,
        
    }
    
    return render(request, "pages/home.html", data)

# to display the about page
def about(request):
    teams = Team.objects.all()
    
    data = {
    'teams' : teams,
    
    }
    return render(request, "pages/about.html", data)

# to display serbvices page
def services(request):
    return render(request, "pages/services.html")

#  to display contact page
def contact(request):
    return render(request, "pages/contact.html")