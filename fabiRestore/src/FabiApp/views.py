from django.shortcuts import get_object_or_404, redirect, render

from .models import Meuble


def accueil(request):
    return render(request, 'FabiApp/accueil.html')

def apropos(request):
    return render(request, 'FabiApp/apropos.html')

def contact(request):
    return render(request, 'FabiApp/contact.html')

def vitrine(request):
    context = {"meubles" : Meuble.objects.all().order_by('date')}
    return render(request, 'FabiApp/vitrine.html', context)

def show(request, meuble_id):
    context = {"meuble": get_object_or_404(Meuble, pk = meuble_id)}
    return render(request, "FabiApp/show.html", context)
