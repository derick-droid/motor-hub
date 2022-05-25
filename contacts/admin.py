from django.contrib import admin
from .models  import contacts
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "car_title", "city", "create_date")
    list_display_links =  ("id", "first_name", "last_name", "email", "car_title", "city", "create_date")
    search_fields = ("id", "first_name", "last_name", "email", "car_title", "city", "create_date")
    list_per_page: 25
admin.site.register(contacts, ContactAdmin)