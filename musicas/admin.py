from django.contrib import admin
from .models import Musica, MusicaArtista, Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
campo = list(UserAdmin.fieldsets)
campo.append(
    ("Histórico", {'fields':('musica_visto', 'foto_perfil')})
)

UserAdmin.fieldsets = tuple(campo)


admin.site.register(Musica)
admin.site.register(MusicaArtista)
admin.site.register(Usuario, UserAdmin)
