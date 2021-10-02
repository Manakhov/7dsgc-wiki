from django.shortcuts import get_object_or_404
from .models import Heroes


def get_one_hero(pk):
    """Getting one hero from Heroes database"""
    hero = get_object_or_404(Heroes, pk=pk)
    return hero
