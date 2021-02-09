from .models import Heroes, Properties
from django.forms import ModelForm, Form, TextInput, Textarea, Select, CheckboxSelectMultiple, MultipleChoiceField


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
                'placeholder': 'Введите имя'
            }),
            'icon': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте адрес иконки'
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
                'placeholder': 'Введите свойство'
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

    class Meta:
        model = Heroes
        fields = ['uniqueness',
                  'properties',
                  ]
        widgets = {
            'uniqueness': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Фильтр по уникальности'
            }),
            'properties': CheckboxSelectMultiple()
        }