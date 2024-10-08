from django import forms
from .models import Meuble, Auteur

class FormClassique(forms.Form):
    username = forms.CharField(label = "Nom d'utilisateur", max_length=32, required=True)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    publier = forms.CharField(label = "Publier ?", widget=forms.CheckboxInput)

    langues = [("f", "Francais"), ("a", "Anglais")]
    langue = forms.MultipleChoiceField(label="Choix de la langue", widget=forms.CheckboxSelectMultiple, choices=langues)

    colors = [('1', 'Rouge'), ('2', 'Bleu'), ('3', 'Vert')]
    color = forms.ChoiceField(label= "Choix de la couleur", choices=colors, widget=forms.RadioSelect)

    pays = [('1', 'France'), ('2', 'Japon'), ('3', 'Espagne')]
    paysChoice = forms.ChoiceField(label= "Choix de pays", choices=pays)

class FormMeuble(forms.ModelForm):

    # auteurs = forms.ModelChoiceField(queryset = Auteur.objects.all(), label = "Auteur")

    class Meta:
        model = Meuble
        fields = ['titre', 'auteur', 'couleur', 'prix', 'date']
        labels = {'titre': 'Titre', 'auteur': 'Auteur', 'prix': 'Prix'}
    
    #méthode de validation custom pour un champ en particulier du form
    def clean_prix(self):
        prix = self.cleaned_data['prix']
        if prix <= 0:
            raise forms.ValidationError("Le prix du meuble doit être supérieur à zéro")
        return prix
    
    #méthode de validation custom pour l'ensemble du form
    def clean(self):
        auteur = self.cleaned_data['auteur']
        prix = self.cleaned_data['prix']

        if str(auteur) == "FabiRestore" and prix < 150 :
            raise forms.ValidationError("Le prix d'un meuble réalisé par le grand Fabi Restore doit être supérieur à 150€")
        
        return self.cleaned_data