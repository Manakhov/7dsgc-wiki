from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Heroes
from .forms import HeroesForm, PropertiesForm, FilterForm


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
    heroes = Heroes.objects.filter(**filter_dict).order_by('-rank', 'name')
    context = {'title': 'All heroes 7ds-gc',
               'filter_form': filter_form,
               'heroes': heroes,
               }
    return render(request, 'main/all_heroes.html', context)


def one_hero(request, pk):
    hero = get_object_or_404(Heroes, pk=pk)
    context = {'hero': hero,
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
