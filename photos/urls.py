from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', photo_list, name='photo_list'),
    url(r'^(\d+)$', photo_detail, name='photo_detail'),
]