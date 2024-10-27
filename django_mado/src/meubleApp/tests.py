from django.test import TestCase
from .models import Auteur
from types import MethodType
from django.test.runner import DiscoverRunner
from django.db import connections



class AuteurTestCase(TestCase):

    # classe qui définit l'environnement pour tous les tests
    def setUp(self):
        self.auteur = Auteur.objects.create(nom='Louis', age=23)
         
    def test_is_correct_instance(self):
        self.assertIsInstance(self.auteur, Auteur)

    def test_exists(self):
        auteur = Auteur.objects.get(nom='Louis')
        self.assertTrue(auteur)

    
