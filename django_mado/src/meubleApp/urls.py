from django.urls import path
from . import views

app_name = "meubleApp"   # Bonne pratique, il faut par contre rajouter le app_name quand on va importer des url dans les html. exemple "{ url appname:urlName }"

urlpatterns = [
    path('', views.index, name='index_meubleApp'), # /meuble
    path('liste/', views.madoList, name='liste_meuble'), # /meuble/liste
    path('<int:meuble_id>', views.show, name='show'), # ex : /meuble/1
    path('dbVide/', views.RemplirSiDBVide, name='dbVide'),   # /meuble/dbVide
    path('form/', views.formulaire, name='formulaire'), # /meuble/form
    path('listing/', views.listing, name='listing_meuble'), # /meuble/listing
    path('deleteMeuble/<int:meuble_id>', views.delete, name='delete_meuble'), # /meuble/deleteMeuble/1
    path('addMeuble/', views.ajout_meuble, name='ajout_meuble'), # /meuble/addMeuble
    path('modifMeuble/<int:meuble_id>', views.modif_meuble, name='modif_meuble'), # /meuble/modifMeuble/1
]