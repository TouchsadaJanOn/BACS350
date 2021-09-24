from django.db import models

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
