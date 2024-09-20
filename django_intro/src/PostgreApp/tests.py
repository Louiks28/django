from django.test import TestCase

from .models import User, UserList

# Create your tests here.

class UserTestCase(TestCase):

    USERNAME = "louisky"
    LAST_NAME = "Calux"
    FIRST_NAME= "Louis"

    # set up pour initialiser ce dont on a besoin pour nos tests
    def setUp(self):
        self.list_de_test = UserList()
        self.list_de_test.name="Liste de test"
        self.list_de_test.save()

        self.user_test = User()
        self.user_test.username = self.USERNAME
        self.user_test.last_name = self.LAST_NAME
        self.user_test.first_name = self.FIRST_NAME
        self.user_test.user_list = self.list_de_test
        self.user_test.save()


    def test_create_user(self):

        nbr_de_users = User.objects.count()

        newUser = User()
        newUser.username='Manren'
        newUser.email='manon@gmail.com'
        newUser.last_name='Renaud'
        newUser.first_name='Manon'
        newUser.user_list=self.list_de_test
        newUser.save()

        nbr_de_users_apres_ajout = User.objects.count()

        self.assertTrue(nbr_de_users_apres_ajout == nbr_de_users+1)

    
    def test_update_user(self):

        self.assertEqual(self.USERNAME, self.user_test.username)

        self.user_test.username="mickadow"
        self.user_test.save()

        tempElement =  User.objects.get(pk=self.user_test.pk)

        self.assertEqual(tempElement.username, "mickadow")


    def test_delete_user(self):

        nbr_de_users = User.objects.count()

        self.user_test.delete()

        nbr_de_users_apres_delete = User.objects.count()

        self.assertTrue(nbr_de_users_apres_delete == nbr_de_users-1)
