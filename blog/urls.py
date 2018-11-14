from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add_movie/', views.add_movie, name='blog-add_movie'),
    path('search_movie/', views.search_movie, name='blog-search_movie'),
    path('list_all/', views.list_all, name='blog-list_all'),
    
]