from django.contrib import admin
from .models import Produto

# Register your models here.

"""
Caso você queira ver seus modelos no painel de admin
você deve importá-los aqui e utilizar um dos métodos a seguir:
"""

#Esta linha habilita a possibilidade de adicionar e registrar produtos
#direto pelo painel de admin com uma visualização básica

# admin.site.register(Produto) 

#Mas podemos fazer melhor do que isso!
#Podemos fazer uma classe para administração!

#Descomente o código abaixo para visualizar um painel com mais opções.

class ProdutoAdmin(admin.ModelAdmin):
    #Campos exibidos na lista de produtos
    list_display = ('nome', 'preco', 'id') 
    
    #Campos pelos quais é possível filtrar a lista
    list_filter = ('preco',) 
    
    #Adiciona uma caixa de pesquisa para buscar por nome
    search_fields = ('nome',)
    
    #Ordenação por nome (se quiser né)
    ordering = ('nome',)
    
    #Tornar o preço editável diretamente na lista
    list_editable = ('preco',)

#Adicionamos então a linha anterior, mas com um painel bonito!
admin.site.register(Produto, ProdutoAdmin)