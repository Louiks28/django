# Generated by Django 4.2.16 on 2024-10-08 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meubleApp', '0002_meuble_titre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auteur',
            options={'verbose_name': 'Auteur', 'verbose_name_plural': 'Auteurs'},
        ),
        migrations.AlterModelOptions(
            name='meuble',
            options={'verbose_name': 'Meuble', 'verbose_name_plural': 'Meubles'},
        ),
        migrations.AlterField(
            model_name='meuble',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
