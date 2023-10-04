from django.contrib import admin
from .models import Musica, MusicaArtista
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Musica)
admin.site.register(MusicaArtista)

