from ast import keyword
from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    cars = Car.objects.order_by("-created_date") # extracting data fromthe database
    paginator = Paginator(cars, 4) # creating pages
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    
    # search functionality in cars page
    model_search = Car.objects.values_list("model", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    body_search = Car.objects.values_list("body_style", flat=True).distinct()
    
    data = {
        "cars" : cars,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_search' : body_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk = id)
    
    data = {
        "single_car" : single_car
    }
    
    return render(request, 'cars/car_detail.html', data)


def search(request):
    # bringing data from the database
    cars = Car.objects.order_by("-created_date")
    
     # search functionality in cars page
    model_search = Car.objects.values_list("model", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    body_search = Car.objects.values_list("body_style", flat=True).distinct()
    transmission_search = Car.objects.values_list("transmission", flat=True).distinct()
    
    # enable such functionality with keys
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains = keyword)
            
    # enable search functionality with model
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact = model)
    
    # enable search functionality with year        
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact = year)
            
    # enable search functionality with body style
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact = body_style)
            
    # enable search by transmission 
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact = transmission)
            
    # enable search functionality with minimum and maximum prices
    if 'min_price' in request.GET:
        min_prie = request.GET['min_price']
        max_price = request.GET['max_price']
        
        if max_price:
           cars =  cars.filter(price__gte = min_prie, price__lte = max_price)
    
    data = {
        "cars" : cars,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_search' : body_search,
        'transmission_search' : transmission_search
    }
    return render (request, "cars/search.html", data)