from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_heroes, name='all_heroes'),
    path('hero', views.one_hero, name='one_hero'),
    path('new', views.new_hero, name='new_hero'),
]
