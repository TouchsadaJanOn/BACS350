from django.db import models
from django.urls.base import reverse_lazy
# Create your models here.


class Superhero(models.Model):

    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    description = models.TextField(default="none")
    strength = models.CharField(max_length=100, default="none")
    weakness = models.CharField(max_length=100, default="none")
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} who is {self.identity}'

    def get_absolute_url(self):
        return reverse_lazy('hero_details', args=[str(self.id)])
