from django.urls import path
from .views import Home, Artistas, DetalheArtista, PesquisaMusica
from django.contrib.auth import views as auth_view

app_name = 'musica'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('artistas/', Artistas.as_view(), name='artista'),
    path('artistas/<int:pk>', DetalheArtista.as_view(), name='detalheartista'),
    path('pesquisa/', PesquisaMusica.as_view(), name='pesquisamusica'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
