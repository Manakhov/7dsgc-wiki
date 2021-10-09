from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_heroes, name='all_heroes'),
    path('hero_<int:pk>', views.one_hero, name='one_hero'),
    path('create', views.create_hero, name='create_hero'),
]
