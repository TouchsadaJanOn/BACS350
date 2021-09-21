#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Superhero

admin.site.register(Book)
admin.site.register(Superhero)
