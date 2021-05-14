from django import forms
from .models import *

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'telefone','data_aniversario','grupo_membro','ministerios']

        widgets = {
            'nome': forms.TextInput(attrs={
            'class': 'form-control',
            'style': '',
            'placeholder': 'Nome',
            }),
            'telefone': forms.TextInput(attrs={
            'class': 'form-control',
            'style': '',
            'placeholder': 'Telefone'
            }),
            'data_aniversario': forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'placeholder': 'Data de Aniversário'
            }), 
            'grupo_membro': forms.Select(attrs={
            'class': 'form-control',
            'style': '',
            'placeholder': 'Grupos'
            }),
            'ministerios': forms.Select(attrs={
            'class': 'form-control',
            'style': '',
            'placeholder': 'Ministérios'
            }),
         }

