from rest_framework import serializers

from .models import User, UserList

# La classe serializer va faire le lien entre la BDD et le format de réponse de l'API(json..)


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
        