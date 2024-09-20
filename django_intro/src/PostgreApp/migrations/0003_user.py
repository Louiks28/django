# Generated by Django 4.2.16 on 2024-09-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostgreApp', '0002_userlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='PostgreApp.userlist')),
            ],
        ),
    ]