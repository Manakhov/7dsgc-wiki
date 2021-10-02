from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Heroes
from .forms import HeroesForm


def get_one_hero(pk):
    """Getting one hero from Heroes database"""
    hero = get_object_or_404(Heroes, pk=pk)
    return hero


def add_hero(request):
    """Adding hero in Heroes database"""
    heroes_form = HeroesForm(request.POST)
    if heroes_form.is_valid():
        heroes_form.date_change = timezone.now()
        heroes_form.save()
    else:
        return False
