from django.db import models
from django.contrib.auth.models import User

# Modèle "perso" lié à la classe User de Django

class UserProfile(models.Model):

    account = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=16)
    lucky_number = models.IntegerField()