from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('wish', views.wish),
    path('wishes', views.wishes),
    path('delete/<int:id>', views.delete),
]