from django.contrib import admin
from .models import Todo

#allows each todo entry to be managed from the admin portal
admin.site.register(Todo)
