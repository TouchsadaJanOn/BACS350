from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Book
# Create your views here.


class BookView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book
