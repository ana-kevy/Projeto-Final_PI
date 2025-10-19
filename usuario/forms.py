from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'cpf', 'endereco', 'curriculo', 'habilidades', 
            'link_portfolio', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, número, complemento'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'habilidades': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva suas principais habilidades'}),
            'link_portfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://meuportfolio.com'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Crie uma senha forte',
            'id': 'id_password1'
        })
    
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Repita a senha',
            'id': 'id_password2'
        })
        
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar Senha'
        self.fields['email'].required = True
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
