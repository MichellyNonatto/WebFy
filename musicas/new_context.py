from .models import Musica

def recentes(request):
    lista_artistas = Musica.objects.all().order_by('-dataCriacao')[0:5]
    return {'recentes': lista_artistas}

def visualizados(request):
    lista_artistas = Musica.objects.all().order_by('visualizacoes')[0:5]
    return {'visualizados': lista_artistas}