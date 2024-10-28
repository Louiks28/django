from django.urls import path
from . import views

app_name = "FabiApp"   # Bonne pratique, il faut par contre rajouter le app_name quand on va importer des url dans les html. exemple "{ url appname:urlName }"

urlpatterns = [
    path('', views.accueil, name='accueil_FabiRestore'), # /fabirestore
]