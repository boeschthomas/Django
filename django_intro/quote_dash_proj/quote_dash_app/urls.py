from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.quotes),
    path('login', views.quotes),
    path('logout', views.login),
    path('create_quote', views.quotes)
]