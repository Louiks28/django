from rest_framework import routers

from .views import UserViewSet, UserListViewSet

# Ici la classe url permet d'enregistrer les différentes routes de notre API

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('userList', UserListViewSet)