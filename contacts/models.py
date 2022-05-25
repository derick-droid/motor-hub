import email
from django.db import models
from datetime import datetime

class contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_nedd = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    message = models.TextField(blank = True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateField(blank=True, default=datetime.now)
    
    def __str__(self):
        return email

    