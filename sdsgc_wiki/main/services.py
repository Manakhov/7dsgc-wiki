from django.shortcuts import get_object_or_404
from django.utils.timezone import now as timezone_now
from django.contrib.auth import login, authenticate
from .models import Heroes


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


def add_hero(heroes_form):
    """Adding hero in Heroes database"""
    if heroes_form.is_valid():
        new_heroes_form = heroes_form.save(commit=False)
        new_heroes_form.date_change = timezone_now()
        new_heroes_form.save()
        heroes_form.save_m2m()
        return True
    return False


def add_property(properties_form):
    """Adding property in Properties database"""
    if properties_form.is_valid():
        properties_form.save()
        return True
    return False


def add_user(user_form):
    """Adding user in Users database"""
    if user_form.is_valid():
        user_cleaned_data = user_form.cleaned_data
        new_user_form = user_form.save(commit=False)
        new_user_form.set_password(user_cleaned_data['password'])
        new_user_form.save()
        return True
    return False


def delete_one_hero(pk):
    """Deleting hero from Heroes database"""
    get_object_or_404(Heroes, pk=pk).delete()


def user_login(request, user_form):
    """Logging user"""
    errors = user_form.errors  # does not work without this line
    user_cleaned_data = user_form.cleaned_data
    if 'username' in user_cleaned_data.keys():
        user = authenticate(username=user_cleaned_data['username'], password=user_cleaned_data['password'])
    else:
        user = authenticate(username=request.POST['username'], password=user_form.cleaned_data['password'])
    if user is not None and user.is_active:
        login(request, user)
        return True
    return False
