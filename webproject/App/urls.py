from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^servicios/$', views.services, name='services'),
    re_path(r'^tienda/$', views.shop, name='shop'),
    re_path(r'^contacto/$', views.contact, name='contact'),
    re_path(r'^blog/$', views.blog, name='blog'),
]