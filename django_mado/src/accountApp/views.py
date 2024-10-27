from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm


# login_user 
# logout_user
# register_user

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Si l'authent est correct
        if user is not None:
            login(request, user)
            return redirect("meubleApp:listing_meuble")
            # return redirect("meubleApp:listing")
        # Si l'authent est incorrect
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")

    form = AuthenticationForm()
    return render(request, "accountApp/login.html", {"form": form})



def logout_user(request):
    logout(request)
    return redirect("meubleApp:listing_meuble")

def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("meubleApp:listing_meuble")
    else:
        form = NewUserForm()
    return render(request, "accountApp/register.html", {"form": form})


