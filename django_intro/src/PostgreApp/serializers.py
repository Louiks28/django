from rest_framework import serializers

from .models import User, UserList


class UserSerializer(serializers.ModelSerializer):

    #Pour remplacer le nom d'attribut en retour d'API
    Username = serializers.CharField(source="username")

    class Meta:
        model = User
        exclude = ['username']

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserList
        fields = '__all__'
        