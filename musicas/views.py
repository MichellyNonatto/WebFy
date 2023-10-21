from django.shortcuts import render, redirect, reverse
from .models import Musica, MusicaArtista, Usuario
from .forms import CriarContaForm, FormHome
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class Home(FormView):
    template_name = "home.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('musicas:artistas')
        else:
            return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('musicas:login')
        else:
            return reverse('musicas:criarconta')


class Artistas(LoginRequiredMixin, ListView):
    template_name = "artistas.html"
    model = Musica

    def get_queryset(self):
        return Musica.objects.all().order_by('titulo')


class DetalheArtista(LoginRequiredMixin, DetailView):
    template_name = "detalheartista.html"
    model = Musica

    def get(self, request, *args, **kwargs):
        musica = self.get_object()
        musica.visualizacoes += 1
        musica.save()
        usuario = request.user
        usuario.musica_visto.add(musica)
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

class PesquisaMusica(LoginRequiredMixin, ListView):
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


class PaginaPerfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('musicas:login')