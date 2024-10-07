from django import forms

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