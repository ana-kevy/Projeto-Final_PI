from django import forms
from .models import Vaga, Mensagem

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'requisitos', 'salario', 'ativo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da vaga'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva a vaga'}),
            'requisitos': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Liste os requisitos'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salário (opcional)'}),
        }


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Digite sua mensagem...'
            }),
        }
