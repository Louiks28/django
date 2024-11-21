from django.test import TestCase

from .models import Meuble, Photo

# Test sur les modèles Meuble et Photo
class MeubleTestCase(TestCase):

    def setUp(self):
        self.meuble = Meuble.objects.create(titre='Buffet mado vintage',  #CharField
                                            statut="Disponible",  #CharField
                                            date='2024-11-21',  #CharField AAAA-MM-JJ
                                            couleurs='beige et marron',  #CharField
                                            prix=350,  #DecimalField
                                            description='Buffet en bois de chêne',  #CharField
                                            longueur=120,  #DecimalField
                                            profondeur=60,  #DecimalField
                                            hauteur=140,  #DecimalField
                                            photoCouverture='couvertures/couv_defaut.jpg',  #ImageField
                                            categorie='Buffet')  #CharField
        
        self.photo = Photo.objects.create(meuble=self.meuble,  #Meuble
                                         image='couvertures/couv_defaut.jpg')  #ImageField

    def test_is_correct_instance_meuble(self):
        self.assertIsInstance(self.meuble, Meuble)

    def test_is_correct_instance_photo(self):
        self.assertIsInstance(self.photo, Photo)

    def test_exists_meuble(self):
        meuble = Meuble.objects.get(titre='Buffet mado vintage')
        self.assertTrue(meuble)

    def test_exists_photo(self):
        photo = Photo.objects.filter(meuble__titre='Buffet mado vintage')
        self.assertTrue(photo)

