from django.conf.urls import url, include
from .views import add_a_rating

urlpatterns = [
    url(r'^add/$', add_a_rating, name='add_a_rating'),
]