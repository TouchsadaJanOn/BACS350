from django.test import TestCase
from django.urls import reverse

from .models import Article


class ArticleViewsTest(TestCase):

    def login(self):
        response = self.client.login(
            username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def test_article_list_view(self):
        Article.objects.create(**self.article1)
        self.assertEqual(reverse('article_list'), '/article/')
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_article_detail_view(self):
        self.assertEqual(reverse('article_detail', args='1'), '/article/1')
        self.assertEqual(reverse('article_detail', args='2'), '/article/2')
        Article.objects.create(**self.article1)
        response = self.client.get('/article/1')
        self.assertEqual(response.status_code, 200)

    def test_article_add_view(self):

        # Add without Login
        response = self.client.post(reverse('article_add'), self.article1)
        self.assertEqual(response.url, '/accounts/login/?next=/article/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('article_add'), self.article1)
        response = self.client.post(reverse('article_add'), self.article2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/article/')
        self.assertEqual(len(Article.objects.all()), 2)

        # List the articles
        response = self.client.get('/article/')
        self.assertContains(response, '<tr>', count=3)

    def test_article_edit_view(self):

        # Edit without Login
        Article.objects.create(**self.article1)
        self.assertEqual(reverse('article_edit', args='1'), '/article/1/')
        response = self.client.get('/article/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/article/1/')

        # Login to edit
        self.login()
        response = self.client.post('/article/1/', self.article2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/article/')

        # Check the book object
        c = Article.objects.get(pk=1)
        self.assertEqual(c.title, self.article2['title'])
        self.assertNotEqual(c.title, self.article1['title'])
        self.assertEqual(c.document, self.article2['document'])

    def test_article_delete_view(self):
        self.login()
        Article.objects.create(**self.article1)
        self.assertEqual(reverse('article_delete', args='1'),
                         '/article/1/delete')
        response = self.client.get('/article/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/article/1/delete')
        self.assertEqual(len(Article.objects.all()), 0)
