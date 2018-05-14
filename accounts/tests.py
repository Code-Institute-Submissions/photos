from django.test import TestCase
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.shortcuts import render_to_response
from .views import *

# Create your tests here.


class TestAccounts(TestCase):
    def test_anonymous_user_can_not_view_profile(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)
        
    def test_logged_in_user_can_view_profile(self):
        user = User.objects.create_user('user', 'user@example.com', 'user')
        self.client.login(username="user", password="user")

        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
        
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'joe',
            'email': 'joe@joe.com',
            'password1': 'joe12345',
            'password2': 'joe12345',
        })
 
        self.assertTrue(form.is_valid())
    
    def test_login_page_resolves(self):
        login_page = resolve("/accounts/login")
        self.assertEqual(login_page.func, login)
        
    def test_register_page_resolves(self):
        register_page = resolve("/accounts/register")
        self.assertEqual(register_page.func, register)    
       
    def test_profile_page_resolves(self):
        profile_page = resolve("/accounts/profile")
        self.assertEqual(profile_page.func, profile)    
        
    
    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/accounts/login')
        self.assertEqual(home_page.status_code, 200)
    
    
    def test_login_template(self):
        response = self.client.get('/accounts/login')
        self.assertTemplateUsed(response, 'accounts/login.html')
    