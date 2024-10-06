from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

import datetime

from .models import Meuble


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
