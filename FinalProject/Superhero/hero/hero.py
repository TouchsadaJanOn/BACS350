from django.contrib.auth import get_user_model
from os.path import exists
from markdown import markdown

from hero.models import Superhero, Article


# def get_author(name):
#     return Author.objects.get(name=name)


def get_book(title):
    return Superhero.objects.get(title=title)


def create_article(**kwargs):
    title = kwargs.get('title')
    # author = kwargs.get('author')
    article = Superhero.objects.get_or_create(title=title)[0]
    article.doc_path = kwargs.get('doc_path')
    article.description = kwargs.get('description')
    article.save()
    return article


def get_article(hero, order):
    c = Article.objects.get(hero=hero, order=order)
    c.markdown = open(f'Documents/Article/{c.document}.md').read()
    c.html = markdown(c.markdown)
    c.save()
    return c
