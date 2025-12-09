from .models import Produto # Importa o Model Produto que acabamos de criar
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página funcionando!")

def listar_produtos(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    todos_produtos = Produto.objects.all()
    
    #Cria uma lista de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in todos_produtos]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_de_nomes)}")