from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
# from django.views.generic.base import TemplateView
from markdown import markdown

from .models import Article


class ArticleView(RedirectView):
    url = '/article/'


class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article

    def get_queryset(self):
        return super().get_queryset()


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        article = kwargs['object']
        article.markdown = open('Documents/Article/article1.md').read()
        article.html = markdown(article.markdown)
        article.save()
        return kwargs


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_add.html"
    model = Article
    fields = ['hero', 'order', 'title', 'markdown']
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article_edit.html"
    model = Article
    fields = ['hero', 'order', 'title', 'markdown']
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
