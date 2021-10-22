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


class Article(models.Model):
    # pointer to Superhero object
    hero = models.CharField(max_length=20, default='none')
    order = models.IntegerField  # superhero order
    title = models.CharField(max_length=200)  # title text of the superhero
    markdown = models.TextField()  # markdown text
    html = models.TextField()

    def export_record(self):
        return [self.hero, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Article.objects.get_or_create(hero=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()

    def __str__(self):
        return f'{self.hero.title} - {self.order} - {self.title}'
