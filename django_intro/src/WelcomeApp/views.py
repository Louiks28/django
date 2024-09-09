from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1> Page d'acceuil de notre application </h1>")

def article(request, num_article):
    if num_article in ["1", "2", "3"] :
        return render(request, f"article{num_article}.html")
    return render(request, "article_notFound.html")
