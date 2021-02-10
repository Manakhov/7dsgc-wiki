from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Heroes
from .forms import HeroesForm, PropertiesForm, FilterForm


def all_heroes(request):
    heroes = Heroes.objects.order_by('name')
    filter_form = FilterForm()
    if 'add_filter' in request.POST:
        filter_form = FilterForm(request.POST)
        errors = filter_form.errors           # does not work without this line
        filter_cleaned_data = filter_form.cleaned_data
        for key in filter_cleaned_data.keys():
            if key == 'color':
                heroes = heroes.filter(color__in=filter_cleaned_data[key])
            if key == 'race':
                heroes = heroes.filter(race__in=filter_cleaned_data[key])
            if key == 'properties':
                selected_properties = []
                for prop in filter_cleaned_data[key]:
                    selected_properties.append(prop.name)
                heroes = heroes.filter(properties__name__in=selected_properties).distinct()
            if key == 'uniqueness':
                heroes = heroes.filter(uniqueness__contains=filter_cleaned_data[key])
    heroes_R = heroes.filter(rank='R')
    heroes_SR = heroes.filter(rank='SR')
    heroes_SSR = heroes.filter(rank='SSR')
    context = {'title': 'All heroes from 7dsgc',
               'filter_form': filter_form,
               'heroes_R': heroes_R,
               'heroes_SR': heroes_SR,
               'heroes_SSR': heroes_SSR,
               }
    return render(request, 'main/all_heroes.html', context)


def one_hero(request):
    heroes = Heroes.objects.order_by('name')
    heroes_R = heroes.filter(rank='R')
    heroes_SR = heroes.filter(rank='SR')
    heroes_SSR = heroes.filter(rank='SSR')
    context = {'title': 'TEST',
               'heroes': heroes,
               'heroes_R': heroes_R,
               'heroes_SR': heroes_SR,
               'heroes_SSR': heroes_SSR,
               }
    return render(request, 'main/one_hero.html', context)


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
