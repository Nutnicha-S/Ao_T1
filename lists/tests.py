from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from django.test import TestCase
from lists.models import Item

from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

class SignUpTest(TestCase):
    def test_user_signup(self):
        self.example_user = User.objects.create_user(username='Panachai', password='mypasswordisveryeasy',
                                                     email='panachai@test.com')
        self.example_user.save()

        example_users = User.objects.all()
        self.assertEqual(example_users.count(), 1)

    def test_many_users_signup(self):
        self.example_user1 = User.objects.create_user(username='Panachai', password='Panachaipasswordisveryeasy',
                                                      email='panachai@test.com')
        self.example_user1.save()
        self.example_user2 = User.objects.create_user(username='Kristamet', password='Kristametpasswordisveryeasy',
                                                      email='Kristamet@test.com')
        self.example_user2.save()
        self.example_user3 = User.objects.create_user(username='Nutnicha', password='Nutnichapasswordisveryeasy',
                                                      email='Nutnicha@test.com')
        self.example_user3.save()
        self.example_user4 = User.objects.create_user(username='Watsawat', password='Watsawatpasswordisveryeasy',
                                                      email='Watsawat@test.com')
        self.example_user4.save()

        example_users = User.objects.all()
        self.assertEqual(example_users.count(), 4)