from django import forms #essa classe irá facilitar a produção de formulários
from .models import Produto #Essa é a classe que contém os campos da tabela SQL mapeada com ORM
from django.contrib.auth.models import User #tabela própria do Django para usuários!
from django.contrib.auth.forms import UserCreationForm #Form próprio do Django para login!

class ProdutoForm(forms.ModelForm): #Repare na Herança!
    class Meta: #Uma classe dentro de outra classe!

        #Duas variáveis vão definir a base da tabela e os campos a serem preenchidos
        model = Produto 
        fields = ['nome', 'preco'] 
        
        #Adiciona classes CSS para estilização (opcional, mas recomendado)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Pão de Fermentação Natural'}),
            'preco': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Ex: 15.50'}),
        }


class RegistroForm(UserCreationForm): #Está é uma classe meta como a anterior!
    email = forms.EmailField(required=True, help_text ="Textinho para você saber que é necessário mesmo!")

    class Meta:
        model = User
        fields = ("username", "email")

""" Repare que não precisamos colocar nenhum campo para a senha!
O UserCreationForm já lida com isso. Para que tudo funcione ainda falta uma generic view e uma rota."""