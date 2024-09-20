from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def testBootstrap(request):
    return render(request, "bootstrap.html")


