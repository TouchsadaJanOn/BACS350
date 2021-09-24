from .models import Superhero
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.


class IndexView(ListView):
    model = Superhero
    template_name = 'index.html'


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
