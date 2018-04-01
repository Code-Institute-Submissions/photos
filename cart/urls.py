from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^add/$', add_to_cart, name='add_to_cart'),
    url(r'^view/$', view_cart, name='view_cart'),
    url(r'^remove/(\d+)$', remove_from_cart, name='remove_from_cart'),
    
]