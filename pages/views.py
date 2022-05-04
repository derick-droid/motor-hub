from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

# to display a home page
def home(request):
    # fetching data from data to the home view
    teams = Team.objects.all() # this fetches all the data from Team model
    data = {
        'teams': teams,
    }
    
    return render(request, "pages/home.html", data)

# to display the about page
def about(request):
    teams = Team.objects.all()
    data = {
    'teams' : teams
    }
    return render(request, "pages/about.html", data)

# to display serbvices page
def services(request):
    return render(request, "pages/services.html")

#  to display contact page
def contact(request):
    return render(request, "pages/contact.html")