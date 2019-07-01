from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('login', views.login),
    url('img', views.img),
    url('contact', views.contact),
    url('', views.register),
]