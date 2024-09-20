from django.db import models

# Create your models here.

class UserList(models.Model):
    name = models.CharField(max_length=200, default='Nom_de_la_liste')


    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_list = models.ForeignKey('UserList', on_delete=models.CASCADE, related_name='users', null=False)

    def __str__(self):
        return self.username
    

class Louis_Test(models.Model):
    name = models.CharField(max_length=200, default='Prénom')





