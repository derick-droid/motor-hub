from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.order_by("-created_date") # extracting data fromthe database
    paginator = Paginator(cars, 3) # creating pages
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    
    data = {
        "cars" : cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk = id)
    
    data = {
        "single_car" : single_car
    }
    
    return render(request, 'cars/car_detail.html', data)