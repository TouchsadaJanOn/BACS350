from django.views.generic.edit import DeleteView
from .models import Superhero
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(ListView):
    model = Superhero
    template_name = 'index.html'


class HeroView(RedirectView):
    url = '/hero/'


class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'


class HeroDetailView(TemplateView):
    model = Superhero
    template_name = 'hero_details.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Superhero.objects.get(pk=hero_id)
        return {'hero': hero}


class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'superhero_add.html'
    fields = ['name', 'identity', 'image',
              'description', 'strength', 'weakness']


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'superhero_edit.html'
    fields = ['name', 'identity', 'image',
              'description', 'strength', 'weakness']


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'superhero_delete.html'
    success_url = reverse_lazy('hero_list')

########


class AccordionView(TemplateView):
    model = Superhero
    template_name = '_accordion.html'
