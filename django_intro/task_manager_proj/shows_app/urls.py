from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new),
    path('shows_create', views.create_shows),
    path('shows', views.shows),   
    path('shows/<int:id>', views.one_shows),
    path('edit/<int:id>', views.shows_edit_page),
    path('update/<int:id>', views.process_edit),
    path('shows/<int:id>/complete', views.delete_shows),
    path('goback', views.goback),
    path('create_shows', views.new),
    path('go_to_show', views.go_to_show)	   
]