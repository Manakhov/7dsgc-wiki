# Generated by Django 3.1.5 on 2021-01-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_heroes_date_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroes',
            name='properties',
            field=models.TextField(blank=True, verbose_name='Свойства'),
        ),
    ]
