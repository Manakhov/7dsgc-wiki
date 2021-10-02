from django.shortcuts import get_object_or_404
from django.utils.timezone import now as timezone_now
from .models import Heroes
from .forms import HeroesForm, PropertiesForm


def get_one_hero(pk):
    """Getting one hero from Heroes database"""
    hero = get_object_or_404(Heroes, pk=pk)
    return hero


def add_hero(request):
    """Adding hero in Heroes database"""
    heroes_form = HeroesForm(request.POST)
    if heroes_form.is_valid():
        heroes_form.date_change = timezone_now
        heroes_form.save()
    else:
        return False


def add_property(request):
    """Adding property in Properties database"""
    properties_form = PropertiesForm(request.POST)
    if properties_form.is_valid():
        properties_form.save()
    else:
        return False
