from rest_framework import routers

from .views import UserViewSet, UserListViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('userList', UserListViewSet)