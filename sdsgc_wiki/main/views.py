from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Heroes, Properties
from .forms import HeroesForm, PropertiesForm


def all_heroes(request):
    heroes_R = Heroes.objects.filter(rank='R').order_by('name')
    heroes_SR = Heroes.objects.filter(rank='SR').order_by('name')
    heroes_SSR = Heroes.objects.filter(rank='SSR').order_by('name')
    properties = Properties.objects.order_by('name')
    context = {'title': 'All heroes from 7dsgc',
               'heroes_R': heroes_R,
               'heroes_SR': heroes_SR,
               'heroes_SSR': heroes_SSR,
               'properties': properties
               }
    return render(request, 'main/all_heroes.html', context)


def one_hero(request):
    return render(request, 'main/one_hero.html')


def new_hero(request):
    if 'add_hero' in request.POST:
        heroes_form = HeroesForm(request.POST)
        if heroes_form.is_valid():
            heroes_form.date_change = timezone.now()
            heroes_form.save()
            return redirect('all_heroes')
    elif 'add_property' in request.POST:
        properties_form = PropertiesForm(request.POST)
        if properties_form.is_valid():
            properties_form.save()
            return redirect('new_hero')
    heroes_form = HeroesForm()
    properties_form = PropertiesForm()
    context = {'title': 'Create new hero',
               'heroes_form': heroes_form,
               'properties_form': properties_form,
               }
    return render(request, 'main/new_hero.html', context)
