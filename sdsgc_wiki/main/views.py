from django.shortcuts import render, redirect
from .forms import HeroesForm, PropertiesForm, FilterForm
from .services import get_one_hero, get_all_heroes, get_filtered_heroes, add_hero, add_property, delete_one_hero


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
    if 'update_hero' in request.POST:
        return redirect('update_hero', pk)
    elif 'delete_hero' in request.POST:
        return redirect('delete_hero', pk)
    context = {'hero': get_one_hero(pk),
               }
    return render(request, 'main/one_hero.html', context)


def create_hero(request):
    if request.user.is_authenticated:
        if 'add_hero' in request.POST:
            heroes_form = HeroesForm(request.POST)
            if add_hero(heroes_form):
                return redirect('all_heroes')
        elif 'add_property' in request.POST:
            properties_form = PropertiesForm(request.POST)
            if add_property(properties_form):
                return redirect('create_hero')
        heroes_form = HeroesForm()
        properties_form = PropertiesForm()
        context = {'title': 'Create new hero',
                   'heroes_form': heroes_form,
                   'properties_form': properties_form,
                   }
        return render(request, 'main/create_hero.html', context)
    else:
        return render(request, 'main/not_authenticated.html')


def update_hero(request, pk):
    if request.user.is_authenticated:
        hero = get_one_hero(pk)
        if 'update_hero' in request.POST:
            heroes_form = HeroesForm(request.POST, instance=hero)
            if add_hero(heroes_form):
                return redirect('one_hero', pk)
        elif 'add_property' in request.POST:
            properties_form = PropertiesForm(request.POST)
            if add_property(properties_form):
                return redirect('update_hero', pk)
        heroes_form = HeroesForm(instance=hero)
        properties_form = PropertiesForm()
        context = {'title': 'Update hero',
                   'heroes_form': heroes_form,
                   'properties_form': properties_form,
                   }
        return render(request, 'main/update_hero.html', context)
    else:
        return render(request, 'main/not_authenticated.html')


def delete_hero(request, pk):
    if request.user.is_authenticated:
        if 'yes' in request.GET:
            delete_one_hero(pk)
            return redirect('all_heroes')
        if 'no' in request.GET:
            return redirect('one_hero', pk)
        hero = get_one_hero(pk)
        context = {'title': 'Delete hero',
                   'hero': hero,
                   }
        return render(request, 'main/delete_hero.html', context)
    else:
        return render(request, 'main/not_authenticated.html')
