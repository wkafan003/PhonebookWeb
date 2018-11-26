from django.contrib import admin
from .models import phonebook,street_table,city_table

# Register your models here.
admin.site.register(phonebook)
admin.site.register(street_table)
admin.site.register(city_table)
