from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Meuble, Photo


def accueil(request):
    return render(request, 'FabiApp/accueil.html')

def apropos(request):
    return render(request, 'FabiApp/apropos.html')

def contact(request):
    return render(request, 'FabiApp/contact.html')

def vitrine(request):
    context = {
        "meubles" : Meuble.objects.all().order_by('-date'),
        "categories" : Meuble.objects.values_list('categorie', flat=True).distinct(),
        "statuts" : Meuble.objects.values_list('statut', flat=True).distinct(),
    }
        

    return render(request, 'FabiApp/vitrine.html', context)

def show(request, meuble_id):

    meuble = get_object_or_404(Meuble, pk = meuble_id)
    photos = meuble.photos.all()
    context = {
                "meuble": meuble ,
                "photos": photos
                # "photos": Photo.objects.all()
               }
    return render(request, "FabiApp/show.html", context)



@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    meubles = Meuble.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['meuble'] != 'none':
            meuble = Meuble.objects.get(id=data['meuble'])
        else:
            meuble = None

        for image in images:
            photo = Photo.objects.create(
                meuble=meuble,
                image=image,
            )

        # return render(request, "FabiApp/show.html", {"meuble": get_object_or_404(Meuble, pk = data['meuble'])})

    context = {'meubles': meubles}
    return render(request, 'FabiApp/add.html', context)
