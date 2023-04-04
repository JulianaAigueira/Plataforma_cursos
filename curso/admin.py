from django.contrib import admin
from .models import Curso, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin # biblioteca gereciar usuário

# criei esse campo porque quero que no admin apareça o campo personalizado de cursos_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('curso_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Curso)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)