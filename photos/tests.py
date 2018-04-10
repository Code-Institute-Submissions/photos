from django.test import TestCase
from .views import *
from django.core.urlresolvers import resolve

# Create your tests here.

class PhotoTests(TestCase):
    # def test_photo_list_resolves(self):
    #     photo_list = resolve('/photos/')
    #     self.assertEqual(photo_list.func, photo_list)

    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
