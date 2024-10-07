from django.urls import path
from . import views

# app_name = "xxx"   Bonne pratique, il faut par contre rajouter le app_name quand on va importer des url dans les html. exemple "{ url appname:urlName }"

urlpatterns = [
    path('', views.index, name='index_meubleApp'), # /meuble
    path('liste/', views.madoList, name='liste_meuble'), # /meuble/liste
    path('<int:meuble_id>', views.show, name='show'), # ex : /meuble/1
    path('dbVide/', views.RemplirSiDBVide, name='dbVide')   # /meuble/dbVide
]