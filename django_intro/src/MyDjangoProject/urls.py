"""
URL configuration for MyDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import index, peche

from PostgreApp.urls import router as users_router
from rest_framework import routers, permissions

from Usermanagement.urls import router as userManagement_router


# from django.urls import re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Cette API permet de gérer les Users",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@louis.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True, #True = si l'utilisateur n'a pas les droits d'utiliser l'API, il peut quand meme la voir dans le Swagger
                #False = on affiche que les API ou on a accès
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.registry.extend(users_router.registry)
router.registry.extend(userManagement_router.registry)


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('peche/', peche),
    path('welcomeApp/', include("WelcomeApp.urls")),
    path('', include("BootApp.urls")),
    path('', include(router.urls)),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
