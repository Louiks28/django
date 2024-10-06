from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=64, unique = True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Meuble(models.Model):
    titre = models.CharField(max_length=100, default="meuble mado")
    date = models.DateField()
    couleur = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Meuble {self.couleur} créé le {self.date} par {self.auteur}"
