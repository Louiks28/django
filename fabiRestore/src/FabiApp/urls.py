from django.urls import path
from . import views

app_name = "FabiApp"   # Bonne pratique, il faut par contre rajouter le app_name quand on va importer des url dans les html. exemple "{ url appname:urlName }"

urlpatterns = [
    path('', views.accueil, name='accueil_FabiRestore'), # /fabirestore
    path('a-propos', views.apropos, name='apropos_FabiRestore'), # /fabirestore/a-propos
    path('contact', views.contact, name='contact_FabiRestore'), # /fabirestore/contact
    path('vitrine', views.vitrine, name='vitrine_FabiRestore'), # /fabirestore/vitrine
    path('<int:meuble_id>', views.show, name='show_FabiRestore'), # ex : /fabirestore/1
]