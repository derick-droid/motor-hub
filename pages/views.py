from django.shortcuts import render
from django.http import HttpResponse

# to display a home page
def home(request):
    return render(request, "pages/home.html")
# to display the about page
def about(request):
    return render(request, "pages/about.html")
# to display serbvices page
def services(request):
    return render(request, "pages/services.html")

#  to display contact page
def contact(request):
    return render(request, "pages/contact.html")