# Generated by Django 4.2.16 on 2024-11-08 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FabiApp', '0002_alter_meuble_couleurs_alter_meuble_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='meuble',
            name='photoCouverture',
            field=models.ImageField(default='couvertures/couv_defaut', upload_to='couvertures/'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='meubles/photos/')),
                ('meuble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='FabiApp.meuble')),
            ],
        ),
    ]
