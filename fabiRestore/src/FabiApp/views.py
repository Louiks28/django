from django.shortcuts import redirect, render


def accueil(request):
    return render(request, 'FabiApp/accueil.html')

