from django.shortcuts import render, redirect
from .models import Heroes
from .forms import HeroesForm


def all_heroes(request):
    heroes_R = Heroes.objects.filter(rank='R').order_by('name')
    heroes_SR = Heroes.objects.filter(rank='SR').order_by('name')
    heroes_SSR = Heroes.objects.filter(rank='SSR').order_by('name')
    context = {'title': 'All heroes from 7dsgc',
               'heroes_R': heroes_R,
               'heroes_SR': heroes_SR,
               'heroes_SSR': heroes_SSR,
               }
    return render(request, 'main/all_heroes.html', context)


def one_hero(request):
    return render(request, 'main/one_hero.html')


def new_hero(request):
    if request.method == 'POST':
        form = HeroesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_heroes')
    form = HeroesForm()
    context = {'form': form
               }
    return render(request, 'main/new_hero.html', context)
