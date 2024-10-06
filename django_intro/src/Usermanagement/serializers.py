from rest_framework import serializers

from django.contrib.auth.models import User

from Usermanagement.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone', 'lucky_number')


class UserSerializer(serializers.ModelSerializer):

    # on importe les attributs de notre classe custom
    profile = UserProfileSerializer(source = 'userprofile') # source = nom du modèle en minuscule

    class Meta:
        model = User
        # choix des inforamtions du user connecté à afficher
        # fields = '__all__'
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile')

