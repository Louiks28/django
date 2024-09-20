from django.urls import path
from .views import testBootstrap

urlpatterns = [
    path("boot/", testBootstrap)
]