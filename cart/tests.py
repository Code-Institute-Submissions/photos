from django.test import TestCase
from django.core.urlresolvers import resolve

from .views import *
# Create your tests here.
class TestCarts(TestCase):
    def test_cart_page_resolves(self):
        cart_page = resolve("/cart/add")
        self.assertEqual(cart.func, add_to_cart)
        