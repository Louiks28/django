# Generated by Django 4.2.16 on 2024-10-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meubleApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meuble',
            name='titre',
            field=models.CharField(default='meuble mado', max_length=100),
        ),
    ]
