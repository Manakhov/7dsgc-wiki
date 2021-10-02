from django.shortcuts import render, redirect
from .forms import HeroesForm, PropertiesForm, FilterForm
from .services import get_one_hero, get_all_heroes, get_filtered_heroes, add_hero, add_property


def all_heroes(request):
    if 'add_filter' in request.POST:
        filter_form = FilterForm(request.POST)
        heroes = get_filtered_heroes(filter_form)
    else:
        filter_form = FilterForm()
        heroes = get_all_heroes()
    context = {'title': 'All heroes 7ds-gc',
               'filter_form': filter_form,
               'heroes': heroes,
               }
    return render(request, 'main/all_heroes.html', context)


def one_hero(request, pk):
    context = {'hero': get_one_hero(pk),
               }
    return render(request, 'main/one_hero.html', context)


def new_hero(request):
    if 'add_hero' in request.POST:
        heroes_form = HeroesForm(request.POST)
        if add_hero(heroes_form):
            return redirect('all_heroes')
    elif 'add_property' in request.POST:
        properties_form = PropertiesForm(request.POST)
        if add_property(properties_form):
            return redirect('new_hero')
    heroes_form = HeroesForm()
    properties_form = PropertiesForm()
    context = {'title': 'Create new hero',
               'heroes_form': heroes_form,
               'properties_form': properties_form,
               }
    return render(request, 'main/new_hero.html', context)
