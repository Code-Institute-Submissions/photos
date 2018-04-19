from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
    url(r'^posts/create', create_post, name='create_post'),
    url(r'^edit_post/(\d+)', edit_post, name='edit_post'),
    url(r'like/(\d+)', like_post, name='like_post'),
    url(r'delete/(\d+)', delete_post, name='delete_post'),
    url(r'^search/$', search_posts, name='search_posts'),
]