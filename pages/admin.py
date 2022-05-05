from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# creating a class to display a variety of features in the admin

class TeamAdmin(admin.ModelAdmin):
    # function to allow display image in the admin panel
    def thumbnail(self, object):
        return format_html('<img src  = " {}" width = "50"/>'.format(object.photo.url))
    
    thumbnail.short_description = "images" # changing the title display to images
    
    list_display = ("id", "thumbnail" ,"first_name", "last_name", "designation","created_date","facebook_link","twitter_link")
   
    # creating links in the models
    list_display_links = ("id", "thumbnail","first_name", "last_name", "designation","created_date","facebook_link","twitter_link")
    
    # creating search bar
    search_fields = ("first_name", "last_name", "designation")
    
    # creating filter box
    list_filter = ("designation",)
    
admin.site.register(Team, TeamAdmin)