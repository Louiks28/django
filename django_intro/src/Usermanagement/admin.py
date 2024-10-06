from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from Usermanagement.models import UserProfile

# Register your models here.

class UserProfileInLine(admin.StackedInline):

    model = UserProfile


class CustomUserAdmin(UserAdmin):

    inlines = (UserProfileInLine, )


# Pour dire qu'on veut venir customiser la classe User par défaut de django (sur la vue Admin) en lui ajoutant notre classe CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
