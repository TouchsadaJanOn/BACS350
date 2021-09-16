"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hero.views import IndexView, HeroListView, HeroDetailView, SpiderManView, AquaManView, BatmanView, CaptainView, DeadPoolView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view()),
    # Project 4
    path('hero/spiderman', SpiderManView.as_view()),
    path('hero/aquaman', AquaManView.as_view()),
    path('hero/deadpool', DeadPoolView.as_view()),
    path('hero/captain', CaptainView.as_view()),
    path('hero/batman', BatmanView.as_view()),

]
