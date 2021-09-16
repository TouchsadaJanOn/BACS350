#from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Hero


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(TemplateView):
    model = Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}


class IndexView(TemplateView):
    template_name = 'index.html'

# Project 4


class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }


class AquaManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Aqua-Man',
            'body': 'My name is Aqua-Man',
            'image': '/static/images/aquaman.jpg'
        }


class DeadPoolView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'DeadPool',
            'body': 'I got curable Cancer and I heal fast!',
            'image': '/static/images/deadpool.jpg'
        }


class BatmanView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Batman',
            'body': 'I am a strong and rich human!',
            'image': '/static/images/batman.jpg'
        }


class CaptainView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Captain America',
            'body': 'I defend this country with my life!',
            'image': '/static/images/captain.jpg'
        }
