"""irish_photos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home
from contact.views import contact
from accounts import urls as account_urls
from photos import urls as photo_urls
from ratings import urls as rating_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from blog import urls as blog_urls
from django.views.static import serve
from django.conf import settings
from django.conf.urls import handler404, handler500
from photos import views as photo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^accounts/', include(account_urls)),
    url(r'^photos/', include(photo_urls)),
    url(r'^ratings/', include(rating_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

handler404 = photo_views.error_404
handler500 = photo_views.error_500
