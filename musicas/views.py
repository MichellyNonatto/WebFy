from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Musica, MusicaArtista

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class Artistas(ListView):
    template_name = "artistas.html"
    model = Musica

    def get_queryset(self):
        return Musica.objects.all().order_by('titulo')


class DetalheArtista(DetailView):
    template_name = "detalheartista.html"
    model = Musica

    def get(self, request, *args, **kwargs):
        musica = self.get_object()
        musica.visualizacoes += 1
        musica.save()
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        import random
        context = super(DetalheArtista, self).get_context_data(**kwargs)
        while True:
            artistas_relacionados = Musica.objects.filter(categoria=self.get_object().categoria)[
                random.randint(0, 5):random.randint(6, 11)]
            if len(artistas_relacionados) < 5 and len(artistas_relacionados) > 0:
                context["artistas_relacionados"] = artistas_relacionados
                return context
            else:
                continue

class PesquisaMusica(ListView):
    template_name = "pesquisa.html"
    model = Musica

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa == "" or termo_pesquisa.isspace():
            return None

        resultados_musicas = Musica.objects.filter(titulo__icontains=termo_pesquisa)
        resultados_artistas = MusicaArtista.objects.filter(titulo__icontains=termo_pesquisa)
        resultados = list(resultados_musicas) + list(resultados_artistas)
        return resultados

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termo_pesquisa'] = self.request.GET.get("query")
        return context
