from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'


class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return { 
            'hero': 'spiderman',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg' }

class AquaManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return { 'hero': 'aquaman',
        'body': 'I am Aqua-Man',
        'image': '/static/images/aquaman.jpg' 
        }


    