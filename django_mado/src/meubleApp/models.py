from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=64, unique = True) 
    #si le nom de l'attribut ne nous va pas, on peut mettre l'option verbose_name (pour l'affichage dans /admin)
    age = models.IntegerField()

    #Pour l'affichage dans /admin
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"

    def __str__(self):
        return self.nom
    

class Meuble(models.Model):
    titre = models.CharField(max_length=100, default="meuble mado")
    date = models.DateField()
    couleur = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    auteur = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)

    #Pour l'affichage dans /admin
    class Meta:
        verbose_name = "Meuble"
        verbose_name_plural = "Meubles"
        # db_table = "" pour personnaliser le nom de la table dans notre BDD (par défaut nomApp_nomModèle)

    def __str__(self):
        return self.titre
