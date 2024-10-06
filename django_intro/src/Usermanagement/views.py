from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from Usermanagement.serializers import UserSerializer

# Create your views here.

class MeViewSet(viewsets.ViewSet) :

    permission_classes = (IsAuthenticated,)

    #description Swagger
    # @swagger_auto_schema(
    #         operation_description='Cette méthode renvoie le user connecté',
    #         responses={200: UserSerializer,
    #                    400: 'Bad request'
    #                    }
    # )


    # Méthode pour récup l'utilisateur qui est connecté

    def list(self, request):

        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)