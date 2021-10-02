from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Heroes
from .forms import HeroesForm, PropertiesForm, FilterForm
from .services import get_one_hero, add_hero, add_property


def all_heroes(request):
    filter_form = FilterForm()
    filter_dict = {}
    if 'add_filter' in request.POST:
        filter_form = FilterForm(request.POST)
        errors = filter_form.errors           # does not work without this line
        filter_cleaned_data = filter_form.cleaned_data
        for key in filter_cleaned_data.keys():
            if key == 'color':
                filter_dict['color__in'] = filter_cleaned_data[key]
            if key == 'race':
                filter_dict['race__in'] = filter_cleaned_data[key]
            if key == 'properties' and filter_cleaned_data[key]:
                selected_properties = []
                for prop in filter_cleaned_data[key]:
                    selected_properties.append(prop.name)
                filter_dict['properties__name__in'] = selected_properties
            if key == 'uniqueness':
                filter_dict['uniqueness__contains'] = filter_cleaned_data[key]
    heroes = Heroes.objects.filter(**filter_dict).distinct().order_by('-rank', 'name')
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
        if add_hero(request):
            return redirect('all_heroes')
    elif 'add_property' in request.POST:
        if add_property(request):
            return redirect('new_hero')
    heroes_form = HeroesForm()
    properties_form = PropertiesForm()
    context = {'title': 'Create new hero',
               'heroes_form': heroes_form,
               'properties_form': properties_form,
               }
    return render(request, 'main/new_hero.html', context)
