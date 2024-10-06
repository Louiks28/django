from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserListSerializer

from .models import User, UserList

# La classe views va recevoir les appels d'API et va appeler les serializers.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    #Securisation de l'appel d'API
    permission_classes = (IsAuthenticated,)
    #ajout de filtres sur la vue User
    filterset_fields = ['date_joined', 'username']
    #ajout de la fonctionnalité recherche (ex: sur le first name) sur la vue User
    search_fields = ['first_name']

class UserListViewSet(viewsets.ModelViewSet):

    queryset = UserList.objects.all()
    serializer_class = UserListSerializer
    #Securisation de l'appel d'API
    permission_classes = (IsAuthenticated,)