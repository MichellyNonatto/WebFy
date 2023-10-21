from django.urls import path
from .views import Home, Artistas, DetalheArtista, PesquisaMusica, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_view

app_name = 'musicas'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('artistas/', Artistas.as_view(), name='artistas'),
    path('artistas/<int:pk>', DetalheArtista.as_view(), name='detalheartista'),
    path('pesquisa/', PesquisaMusica.as_view(), name='pesquisamusica'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/', PaginaPerfil.as_view(template_name='editarperfil.html'), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
]
