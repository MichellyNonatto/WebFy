from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Musica

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
