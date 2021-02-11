from django.db import models
from django.utils import timezone


class Heroes(models.Model):
    name = models.CharField('Имя', max_length=50)
    icon = models.URLField('Иконка')
    rank = models.CharField('Ранг', max_length=3, choices=[(None, 'Выберите ранг'),
                                                           ('SSR', 'SSR'),
                                                           ('SR', 'SR'),
                                                           ('R', 'R')
                                                           ])
    color = models.CharField('Цвет', max_length=7, choices=[(None, 'Выберите цвет'),
                                                            ('Зеленый', 'Зеленый'),
                                                            ('Красный', 'Красный'),
                                                            ('Синий', 'Синий')
                                                            ])
    race = models.CharField('Раса', max_length=10, choices=[(None, 'Выберите расу'),
                                                            ('Богиня', 'Богиня'),
                                                            ('Великан', 'Великан'),
                                                            ('Демон', 'Демон'),
                                                            ('Неизвестно', 'Неизвестно'),
                                                            ('Фея', 'Фея'),
                                                            ('Человек', 'Человек')
                                                            ])
    uniqueness = models.TextField('Уникальность')
    date_change = models.DateTimeField(default=timezone.now)
    properties = models.ManyToManyField('Properties', verbose_name='Свойства', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'


class Properties(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ['name']
