import datetime
from django.db import models

class Meuble(models.Model):

    STATUT_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Vendu', 'Vendu'),
    ]

    titre = models.CharField(max_length=100, default="Meuble mado")
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES)
    date = models.DateField(default=datetime.date.today)
    couleurs = models.CharField(max_length=800)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1200)
    longueur = models.DecimalField(max_digits=10, decimal_places=0)
    profondeur = models.DecimalField(max_digits=10, decimal_places=0)
    hauteur = models.DecimalField(max_digits=10, decimal_places=0)
  

    # #Pour l'affichage dans /admin
    # class Meta:
    #     verbose_name = "Meuble"
    #     verbose_name_plural = "Meubles"
    #     # db_table = "" pour personnaliser le nom de la table dans notre BDD (par défaut nomApp_nomModèle)

    def __str__(self):
        return self.titre
