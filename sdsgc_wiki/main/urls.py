from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_heroes, name='all_heroes'),
    path('hero_<int:pk>', views.one_hero, name='one_hero'),
    path('create_hero', views.create_hero, name='create_hero'),
    path('update_hero_<int:pk>', views.update_hero, name='update_hero'),
    path('delete_hero_<int:pk>', views.delete_hero, name='delete_hero'),
    path('log_out', views.log_out, name='log_out'),
    path('log_in', views.log_in, name='log_in'),
]
