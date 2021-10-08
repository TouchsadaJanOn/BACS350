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

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from hero.views import IndexView, HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView
from django.urls.conf import include, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    # path('', HeroView.as_view()),
    path('hero/', HeroListView.as_view(), name='hero_list'),
    path('hero/<int:pk>', HeroDetailView.as_view(), name='hero_details'),
    path('hero/add', HeroCreateView.as_view(),  name='superhero_add'),
    path('hero/<int:pk>/', HeroUpdateView.as_view(),  name='superhero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='superhero_delete'),

    # User account urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),
]
