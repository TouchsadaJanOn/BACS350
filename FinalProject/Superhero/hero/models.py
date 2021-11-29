from django.db import models
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
# Create your models here.

# --------------------
# Investigator
#
# user - login credentials for investigator
# name - name of Investigator


# class Author(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return f'{self.pk} - {self.name}'


class Superhero(models.Model):

    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    description = models.TextField(default="none")
    strength = models.CharField(max_length=100, default="none")
    weakness = models.CharField(max_length=100, default="none")
    image = models.CharField(max_length=200)
    doc_path = models.CharField(max_length=200, default='Documents')
    # author = models.ForeignKey(
    #     Author, on_delete=models.CASCADE, editable=False, default="none")

    def __str__(self):
        return f'{self.name} who is {self.identity}'

    def get_absolute_url(self):
        return reverse_lazy('hero_details', args=[str(self.id)])


class Article(models.Model):
    # pointer to Superhero object
    hero = models.CharField(max_length=20, default='none')
    order = models.IntegerField()  # superhero order
    # title text of the superhero
    title = models.CharField(max_length=200)
    markdown = models.TextField()  # markdown text
    document = models.CharField(max_length=200, default="none")
    html = models.TextField()
    investigator = models.CharField(max_length=20, default="none")

    def export_record(self):
        return [self.hero, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Article.objects.get_or_create(hero=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()

    @staticmethod
    def create(hero, order, title, document):
        c = Article.objects.get_or_create(hero=hero, order=order)[0]
        c.title = title
        c.document = document
        c.save()
        return c

    def __str__(self):
        return f'{self.hero.title} - {self.order} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_list')
