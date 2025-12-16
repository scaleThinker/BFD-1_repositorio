from django import forms #essa classe irá facilitar a produção de formulários
from .models import Produto #Essa é a classe que contém os campos da tabela SQL mapeada com ORM

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