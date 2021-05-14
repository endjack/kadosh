from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .models import *
from .forms import MembroForm

# Create your views here.

class MembroListView(ListView):
    model= Membro
    template_name = 'index.html'
    context_object_name = 'objMembros'

    def get_queryset(self):
        return Membro.objects.all()

class MembroCreateView(CreateView):
    model = Membro
    form_class = MembroForm
    template_name = 'cadastrar.html'
    #fields = ['nome', 'telefone','data_aniversario','grupo_membro','ministerios']
    success_url = reverse_lazy('index')
   
   

class SobreView(TemplateView):
    template_name = "sobre.html"

