from .models import Produto, Pets, Medicamento, Clientes # Importa o Model Produto que acabamos de criar
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

def consultar_animais(request):
    info_pets = Pets.objects.order_by('idade')

    lista_pets = [item.nome for item in info_pets]
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_pets)}")

def consutar_med(request):
    med_disponivel = Medicamento.objects.filter(disponivel = True)

    lista_med_disp = [item.nome for item in med_disponivel]
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_med_disp)}")

def pai_pet(request):
    info_cliente = Clientes.objects.all()

    lista_cliente = [item.nome for item in info_cliente]
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_cliente)}")