from django.urls import path
from . import views

app_name = "accountApp"

urlpatterns = [
    path('login/', views.login_user, name='login_user'), # /accountApp/login
    path('logout/', views.logout_user, name='logout_user'), # /accountApp/logout
    path('register/', views.register_user, name='register_user'), # /accountApp/register
]