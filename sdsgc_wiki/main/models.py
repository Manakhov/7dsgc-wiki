from django.db import models


class Heroes(models.Model):
    name = models.CharField('Имя', max_length=50)
    rank = models.CharField('Ранг', max_length=3, choices=[('1', 'SSR'), ('2', 'SR'), ('3', 'R')])
    color = models.CharField('Цвет', max_length=7, choices=[('1', 'Зеленый'), ('2', 'Красный'), ('3', 'Синий')])
    race = models.CharField('Раса', max_length=10, choices=[
        ('1', 'Богиня'),
        ('2', 'Великан'),
        ('3', 'Демон'),
        ('4', 'Неизвестно'),
        ('5', 'Фея'),
        ('6', 'Человек')
    ])
    uniqueness = models.TextField('Уникальность')
    # ДОБАВИТЬ ImageField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герои'
