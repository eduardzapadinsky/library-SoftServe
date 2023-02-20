from django.urls import path
from . import views

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('show_authors/', views.show_authors, name='show_authors'),
    path('remove_author/', views.remove_author, name='remove_author'),
]
