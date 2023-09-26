from django.db import models
from django.utils import timezone

# Create your models here.
LISTA_CATEGORIAS = {
    ("ROCK", "Rock"),
    ("POP", "Pop"),
    ("MPB", "MPB"),
    ("PAGODE", "Pagode"),
    ("OUTROS", "Outros"),
}


class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_musicas')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=10, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    dataCriacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class MusicaArtista(models.Model):
    artista = models.ForeignKey(
        "Musica", related_name="musicas", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.artista.titulo + "    -   " + self.titulo
