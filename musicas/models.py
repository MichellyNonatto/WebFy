from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
LISTA_CATEGORIAS = {
    ("ROCK", "Rock"),
    ("POP", "Pop"),
    ("MPB", "MPB"),
    ("PAGODE", "Pagode"),
    ("OUTROS", "Outros"),
}

LISTA_AVATAR = {
    ("avatares/avatar(11).jpg", "Imagem 11"),
    ("avatares/avatar(10).jpg", "Imagem 10"),
    ("avatares/avatar(9).jpg", "Imagem 9"),
    ("avatares/avatar(8).jpg", "Imagem 8"),
    ("avatares/avatar(7).jpg", "Imagem 7"),
    ("avatares/avatar(6).jpg", "Imagem 6"),
    ("avatares/avatar(5).jpg", "Imagem 5"),
    ("avatares/avatar(4).jpg", "Imagem 4"),
    ("avatares/avatar(1).jpg", "Imagem 1"),

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


class Usuario(AbstractUser):
    musica_visto = models.ManyToManyField("Musica", related_name="usuario")
    foto_perfil = models.ImageField(choices=LISTA_AVATAR,  default='avatares/avatar(1).jpg')
