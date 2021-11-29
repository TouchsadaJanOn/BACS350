from django.test import TestCase
from django.urls import reverse
from FinalProject.Superhero.hero.models import Superhero

from hero.models import Superhero


class SuperheroViewsTest(TestCase):

    def login(self):
        response = self.client.login(
            username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('hero_list'))

    def test_hero_list_view(self):
        self.assertEqual(reverse('hero_list'), '/hero/')
        Superhero.objects.create(**self.hero1)
        Superhero.objects.create(**self.hero2)
        response = self.client.get('/hero/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero_list.html')
        self.assertTemplateUsed(response, 'superhero_theme.html')
        self.assertContains(response, '<tr>', count=3)

    def test_hero_detail_view(self):
        Superhero.objects.create(**self.hero1)
        self.assertEqual(reverse('hero_detail', args='1'), '/hero/1')
        self.assertEqual(reverse('hero_detail', args='2'), '/hero/2')
        response = self.client.get(reverse('hero_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_hero_add_view(self):

        # Add without Login
        response = self.client.post(reverse('hero_add'), self.hero1)
        self.assertEqual(response.url, '/accounts/login/?next=/hero/add')
        self.assertEqual(len(Superhero.objects.all()), 0)

        # Login to add
        self.login()
        response = self.client.post(reverse('hero_add'), self.hero1)
        response = self.client.post(reverse('hero_add'), self.hero2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/hero/2')
        response = self.client.get('/hero/')
        self.assertEqual(len(Superhero.objects.all()), 2)

    def test_hero_edit_view(self):

        # Edit without Login
        Superhero.objects.create(**self.hero1)
        self.assertEqual(reverse('hero_edit', args='1'), '/hero/1/')
        response = self.client.get('/hero/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/hero/1/')

        # Login to edit
        self.login()
        response = self.client.post('/hero/1/', self.hero2)
        self.assertEqual(response.url, '/hero/1')
        response = self.client.get(response.url)
        self.assertContains(response, self.hero2['title'])
        self.assertContains(response, self.author1.name)

        # Check the hero object
        hero = Superhero.objects.get(pk=1)
        self.assertEqual(hero.author, self.author1)
        self.assertEqual(hero.title, 'Odyssey')

    def test_hero_delete_view(self):
        self.login()
        Superhero.objects.create(**self.hero1)
        self.assertEqual(reverse('hero_delete', args='1'), '/hero/1/delete')
        response = self.client.get('/hero/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/hero/1/delete')
        self.assertEqual(len(Superhero.objects.all()), 0)
