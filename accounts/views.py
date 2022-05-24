from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       confirm_password = request.POST['confirm_password']
       
       if password == confirm_password: # checking passwords
           #checking username
            if User.objects.filter(username=username).exists():
               messages.error(request, "username already exists ")
               return redirect('register')
           
           # checking for email
            else:
               if User.objects.filter(email=email).exists():
                   messages.error(request, "This email address already exists")
                   return redirect('register')
               
               # if it passes all the details create a user 
               else:
                   user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                   auth.login(request, user)
                   messages.success(request, "You are now logged in ")
                   return redirect('dashboard')
                   user.save
                   messages.success(request, "You are registered successfully ")
                   return redirect('login')
               
           
       else:
           messages.error(request, "password are not the same ")
           return redirect('register')
    else:
         return render(request, "accounts/register.html")

    

def logout(request):
    return redirect("home")

def dashboard(request):
    return render(request, "accounts/dashboard.html")