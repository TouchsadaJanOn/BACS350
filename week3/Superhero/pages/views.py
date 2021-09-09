from django.views.generic import TemplateView

class SpiderManView(TemplateView):
    template_name = 'spiderman.html'

    def get_context_data(self, **kwargs):
        return { 'hero': 'spiderman' }

class AquaManView(TemplateView):
    template_name = "aquaman.html"

    def get_context_data(self, **kwargs):
        return { 'hero': 'aquaman' }

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page', 
            'body': 'Once upon a time ...',
        }
    
    
class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'hero': 'spiderman', 
        }
    
    
class ProfileView(TemplateView):
    template_name = "page.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Profile Page', 
            'body': 'Once upon a time ...',
        }