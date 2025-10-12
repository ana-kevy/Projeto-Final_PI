from django import forms
from .models import Vaga, Mensagem

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['empresa', 'titulo', 'descricao', 'requisitos', 'salario', 'ativo']

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['vaga', 'empresa', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite sua mensagem...'}),
        }
