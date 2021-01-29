from .models import Heroes
from django.forms import ModelForm, TextInput, Textarea, Select


class HeroesForm(ModelForm):
    class Meta:
        model = Heroes
        fields = ["name", "rank", "color", "race", "uniqueness"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите имя"
            }),
            "rank": Select(attrs={
                'class': 'form-control',
            }),
            "color": Select(attrs={
                'class': 'form-control',
            }),
            "race": Select(attrs={
                'class': 'form-control',
            }),
            "uniqueness": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите Уникальность"
            }),
        }