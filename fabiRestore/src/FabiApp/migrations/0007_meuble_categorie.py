# Generated by Django 4.2.16 on 2024-11-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FabiApp', '0006_alter_meuble_photocouverture_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meuble',
            name='categorie',
            field=models.CharField(default='Buffet Mado', max_length=40),
        ),
    ]
