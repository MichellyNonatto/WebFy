from django.urls import path
from .views import Home, Artistas, DetalheArtista

app_name = 'musica'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('artistas/', Artistas.as_view(), name='artista'),
    path('artistas/<int:pk>', DetalheArtista.as_view(), name='detalheartista'),
]
