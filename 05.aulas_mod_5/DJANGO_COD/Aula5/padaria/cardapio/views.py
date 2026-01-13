from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy #Esse método simplifica voltar para um página depois do login
from .models import Produto
from .forms import ProdutoForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User #Importação da tabela de logins!

# Create your views here.

def index(request):

    #Atente-se que para a linha abaixo funcionar
    #Os caminhos dos arquivos html e css precisam ser carregados corretamente!
    return render(request, 'cardapio/index.html',{}) #Este é o formato mais básico para retornar uma página.


@login_required #Com este decorator, só poderá ver a página quem estiver logado! Olha que fácil!
def cadastro_produto(request):
    mensagem_sucesso = None

    """
    Para este caso nós precisamos conferir o tipo da requisição que estamos recebendo.
    Isso porque na requisição GET nós devemos retornar ao usuário apenas o formulário vazio
    Porque esse é provavelmente seu primeiro acesso.

    Se recebemos uma requisição do tipo POST, significa que o usuário está enviando informações
    no formulário, então precisamos lidar com as informações, e responder se houve sucesso ou não.
    """
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid(): #Checa o conteúdo do formulário

            #Salva o objeto no banco de dados se tudo estiver certinho
            produto_salvo = form.save()
            
            #Adiciona uma mensagem de sucesso para o usuário
            mensagem_sucesso = f"Produto '{produto_salvo.nome}' cadastrado com sucesso!"
            
            #Instancia um novo formulário vazio para o usuário cadastrar outro item
            form = ProdutoForm()

            #Repare como podemos trabalhar na view com o formulário sendo uma função
            #Abstraindo totalmente a complexidade, que fica guardada no forms.py

    else: #Se a requisição não for POST

        #Exibe um formulário vazio
        form = ProdutoForm()

    """
    O context é peça fundamental para o Django!
    ele é um dicionário em que você mapeia onde cada variável da sua view
    encontra as variáveis descritas no HTML!
    É assim que ele sabe onde encaixar o que.
    """
    context = {
        'form': form,
        'mensagem_sucesso': mensagem_sucesso
    }

    #Renderiza o template de cadastro
    return render(request, 'cardapio/cadastro_produto.html', context)




#Exemplo da aula 2.
def listar_produtos(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    todos_produtos = Produto.objects.all()

    #"SELECT * FROM Produto"
    
    #Cria um dicionário de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in todos_produtos]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_de_nomes)}")

class RegistroUser(CreateView): #Class based view!!!!
    model = User 
    template_name = 'registration/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('index') #É preciso utilizar o nome da url cadastrada no urls.py, ok?

    #Outro ponto importante de guardar é que para esse modelo de view, o nome dessas variáveis é esperado pelo django.
    #substituir sucess_url por url_de_sucesso causaria erros!