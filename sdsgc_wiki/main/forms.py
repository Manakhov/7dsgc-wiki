from .models import Heroes, Properties
from django.forms import ModelForm, Form, TextInput, Textarea, Select, CheckboxSelectMultiple, CharField,\
    MultipleChoiceField, PasswordInput
from django.contrib.auth.models import User


class HeroesForm(ModelForm):
    class Meta:
        model = Heroes
        fields = ['name',
                  'icon',
                  'rank',
                  'color',
                  'race',
                  'uniqueness',
                  'properties',
                  ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'autocomplete': 'off'
            }),
            'icon': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте адрес иконки',
                'autocomplete': 'off'
            }),
            'rank': Select(attrs={
                'class': 'form-control',
            }),
            'color': Select(attrs={
                'class': 'form-control',
            }),
            'race': Select(attrs={
                'class': 'form-control',
            }),
            'uniqueness': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Уникальность'
            }),
            'properties': CheckboxSelectMultiple()
        }


class PropertiesForm(ModelForm):
    class Meta:
        model = Properties
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите новое свойство',
                'autocomplete': 'off'
            })
        }


class FilterForm(Form, ModelForm):
    color = MultipleChoiceField(widget=CheckboxSelectMultiple, choices=[('Зеленый', 'Зеленый'),
                                                                        ('Красный', 'Красный'),
                                                                        ('Синий', 'Синий')
                                                                        ])
    race = MultipleChoiceField(widget=CheckboxSelectMultiple, choices=[('Богиня', 'Богиня'),
                                                                       ('Великан', 'Великан'),
                                                                       ('Демон', 'Демон'),
                                                                       ('Неизвестно', 'Неизвестно'),
                                                                       ('Фея', 'Фея'),
                                                                       ('Человек', 'Человек')
                                                                       ])
    uniqueness = CharField(required=False, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Уникальность',
        'autocomplete': 'off'
    }))

    class Meta:
        model = Heroes
        fields = ['properties']
        widgets = {
            'properties': CheckboxSelectMultiple()
        }


class UserForm(Form, ModelForm):
    password = CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Введите пароль',
                                                     'autocomplete': 'off'
                                                     }))

    class Meta:
        model = User
        fields = ['username']
        widgets = {'username': TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Введите логин',
                                                'autocomplete': 'off',
                                                })
                   }
