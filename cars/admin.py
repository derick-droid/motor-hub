from django.contrib import admin
from .models import Car
from django.utils.html import format_html



class CarAdmin(admin.ModelAdmin):
     # function to allow display image in the admin panel
    def thumbnail(self, object):
        return format_html('<img src  = " {}" width = "50"/>'.format(object. car_photo.url))
    
    thumbnail.short_description = "car images" # changing the title display to images
    
    list_display = ("id", "car_title", "car_photo", "color","model", "year", "is_featured","fuel_type" , "body_style" ,"price")
    list_display_links = ("id", "car_title", "car_photo", "color","model", "year","fuel_type" , "body_style" ,"price")
    list_editable = ("is_featured",) # to make this feature editable from the admin
    
    # creating search bar
    search_fields = ("id", "car_title","model","color")
    # creating filter
    list_filter = ("model",)
    

admin.site.register(Car,CarAdmin)
