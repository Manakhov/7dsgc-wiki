from django.db import models


class Heroes(models.Model):
    name = models.CharField('Имя', max_length=50)
    icon = models.CharField('Иконка', max_length=200,)
    rank = models.CharField('Ранг', max_length=3, choices=[('SSR', 'SSR'),
                                                           ('SR', 'SR'),
                                                           ('R', 'R')
                                                           ])
    color = models.CharField('Цвет', max_length=7, choices=[('Зеленый', 'Зеленый'),
                                                            ('Красный', 'Красный'),
                                                            ('Синий', 'Синий')
                                                            ])
    race = models.CharField('Раса', max_length=10, choices=[('Богиня', 'Богиня'),
                                                            ('Великан', 'Великан'),
                                                            ('Демон', 'Демон'),
                                                            ('Неизвестно', 'Неизвестно'),
                                                            ('Фея', 'Фея'),
                                                            ('Человек', 'Человек')
                                                            ])
    uniqueness = models.TextField('Уникальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'
