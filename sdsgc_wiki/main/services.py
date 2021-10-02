from django.shortcuts import get_object_or_404
from django.utils.timezone import now as timezone_now
from .models import Heroes
from .forms import HeroesForm, PropertiesForm


def get_one_hero(pk):
    """Getting one hero from Heroes database"""
    hero = get_object_or_404(Heroes, pk=pk)
    return hero


def get_all_heroes():
    """Getting all heroes from Heroes database"""
    heroes = Heroes.objects.order_by('-rank', 'name')
    return heroes


def get_filtered_heroes(filter_form):
    """Getting filtered heroes from Heroes database according to filter_form"""
    filter_dict = {}
    errors = filter_form.errors  # does not work without this line
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
    return heroes


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
