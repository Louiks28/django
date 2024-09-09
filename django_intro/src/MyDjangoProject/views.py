import datetime
from django.http import HttpResponse
from django.shortcuts import render

"""
Fichier où on va stocker nos vues
"""

def index(request):

    date = datetime.date.today()
    return render(request, "index.html", context={"prenom": "Patrick", "date": date})

def peche(request):
    return render(request, "peche.html")