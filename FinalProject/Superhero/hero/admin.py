from django.contrib import admin

# Register your models here.
from .models import Article, Superhero

admin.site.register(Superhero)
admin.site.register(Article)
