from django.test import TestCase
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from .views import *
# Create your tests here.
class TestCarts(TestCase):
    def test_cart_page_resolves(self):
        cart_page = resolve("/cart/add")
        self.assertEqual(cart.func, add_to_cart)
        
    def test_cart_page_status_code_is_ok(self):
        cart_page = self.client.get('/cart/add')
        self.assertEqual(cart_page.status_code, 200)