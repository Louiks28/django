import random
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

import datetime

from meubleApp.forms import FormClassique

from .models import Auteur, Meuble

"""
save() : sauvegarder dans la BDD
create() : create dans la BDD
delete() : delete dans la BDD
SELECT : all(), get()
ORDER BY : order_by('')
LIMIT : [:N]
INSERT : create()
WHERE : filter(titre = "")
        __gt, __lt, __gte, __lte, __startswith

raw("SELECT .....") : pour écrire du sql en dur (en dernier recours)
"""


def index(request):
    # return HttpResponse("Bienvenue sur la page meuble ! ")
    context = {
               "message": "Hello World",
               "number": 15,
               "userList": ('Louis', 'Jean', 'Marie'),
               "dateCreation": datetime.datetime.now(),
               }
    template = loader.get_template("meubleApp/index.html")
    return HttpResponse(template.render(context, request))


def madoList(request):
    context = {"meubles": Meuble.objects.all()}
    return render(request, "meubleApp/madoList.html", context)


def show(request, meuble_id):
    context = {"meuble": get_object_or_404(Meuble, pk = meuble_id)}
    return render(request, "meubleApp/show.html", context)

def listing(request):
    context = {"meubles" : Meuble.objects.all()}
    return render(request, "meubleApp/listing.html", context)

def formulaire(request):
    if request.method == 'POST' :
        form = FormClassique(request.POST)
        if form.is_valid():
            return redirect("meubleApp:formulaire")
    else:
        form = FormClassique()
    context = {"form": form}

    return render(request, "meubleApp/formulaire.html", context)

def delete(request, meuble_id):
    # meuble_to_delete = Meuble.objects.get(filter(titre = meuble_titre)).first()
    meuble_to_delete = get_object_or_404(Meuble, pk = meuble_id)
    meuble_to_delete.delete()
    return redirect("meubleApp:listing_meuble")



def RemplirSiDBVide(request):

    liste_auteurs = ["Jean", "Marie", "Marc", "FabiRestore", "Jeanne"]

    # Vérifier si la table auteur est vide
    if not Auteur.objects.exists() :
        # Ajouter 5 auteurs
        auteurs = [
            Auteur(nom="Jean", age=30),
            Auteur(nom="Marie", age=25),
            Auteur(nom="Marc", age=40),
            Auteur(nom="FabiRestore", age=35),
            Auteur(nom="Jeanne", age=28),
        ]
        Auteur.objects.bulk_create(auteurs)
        # Auteur.save()


    # Vérifier si la table meuble est vide
    if not Meuble.objects.exists() :

       
        # Ajouter 10 meubles
        meubles = []
        for i in range(1, 11):
            auteur = Auteur.objects.get(nom=random.choice(liste_auteurs))
            meubles.append(
                Meuble(
                    titre=f"Meuble {i}",
                    date=datetime.date.today() - datetime.timedelta(days=i),
                    couleur=f"Couleur {i}",
                    prix=100.00 + i * 10.00,
                    auteur=auteur
                )
            )
        Meuble.objects.bulk_create(meubles)
        # Meuble.save()


    return redirect("meubleApp:liste_meuble")
