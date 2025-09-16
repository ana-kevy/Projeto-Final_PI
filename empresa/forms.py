from django import forms
from .models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = [
            'titulo', 'requisitos', 'local',
            'tipo', 'remuneracao', 'carga_horaria', 'empresa'
        ]