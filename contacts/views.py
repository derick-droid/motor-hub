from email import message
from django.shortcuts import render
from .models import contacts
from django.contrib import messages
from contacts.models import Contact
from django.shortcuts import redirect

def inquiry(request):
   if request.method == "POST":
       car_id = request.POST['car_id']
       car_title = request.POST['car_title']
       user_id = request.POST['user_id']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       customer_need = request.POST['customer_need']
       city = request.POST['city']
       state= request.POST['state']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       
       contact = Contact(car_id = car_id, car_title = car_title, 
                         user_id = user_id,first_name = first_name, last_name = last_name,customer_need = customer_need, city = city, state = state, email = email, phone = phone,
                         message = message)
       contacts.save()
       messages.success(request, "message sent successfully , we will reply shortly")
       return redirect("car/" + car_id)