from django.contrib import admin
from .models import User, UserList
# Register your models here.

#Pour afficher les user de la liste quand on est sur notre objet liste dans /admin
class UserInLine(admin.TabularInline):
    model = User
    #pour ne pas afficher de case vide en plus
    extra=0


@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines=(UserInLine,)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('date_joined',)
    ordering = ('date_joined',)