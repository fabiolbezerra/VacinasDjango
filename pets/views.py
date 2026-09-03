from django.http import HttpResponse
from .models import Animal, Raca
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'pets/animais.html'

    def get_queryset(self):
        return Animal.objects.all()


class AnimaisDaRacaView(ListView):
    template_name = 'pets/animais.html'

    def get_queryset(self):
        raca = get_object_or_404(Raca, nome__contains = self.kwargs['raca'])
        return Animal.objects.filter(raca = raca)


class RacasView(ListView):
    template_name = 'pets/racas.html'
    model = Raca


class AnimalView(DetailView):
    template_name = 'pets/animal.html'
    model = Animal


# Código equivalente a implementação da classe IndexView
def index(request):
    animais = Animal.objects.all()
    contexto = { "animal_list": animais, }
    pagina = "pets/animais.html"
    return render(request, pagina, contexto)


# Código equivalente a implementação da classe AnimaisDaRacaView
def animais_raca(request, raca):
    animais = Animal.objects.filter(raca__nome__contains=raca)
    contexto = { "animal_list": animais, }
    pagina = "pets/animais.html"
    template = loader.get_template(pagina)
    pagina_montada = template.render(contexto, request)
    return HttpResponse(pagina_montada)


# Código equivalente a implementação da classe AnimalView
def racas(request):
    racas = Raca.objects.all()
    contexto = { "raca_list": racas, }
    pagina = "pets/racas.html"
    return render(request, pagina, contexto)


# Código equivalente a implementação da classe RacasView
def animal_detail(request, id):
   animal = Animal.objects.get(id = id)
   resposta = f'{animal} - Vacinas: '
   vacinas = animal.vacina_set.all()
   resposta += ", ".join([str(v) for v in vacinas])
   return HttpResponse(resposta)


def hello_world(request):
    return HttpResponse("Hello to django world!")


def hello_world_nome(request, nome):
    return HttpResponse(f"Hello {nome} to django world!")