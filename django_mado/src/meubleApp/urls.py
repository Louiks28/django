from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_meubleApp'), # /meuble
    path('liste/', views.madoList, name='liste_meuble'), # /meuble/liste
    path('<int:meuble_id>', views.show, name='show')
]