from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#A função a seguir irá lidar com a requisição para o index.
def index(request):
    #A View recebe um objeto HttpRequest (request)
    #E deve retornar um objeto HttpResponse
    return HttpResponse("Olá, mundo. Você está no index do meu primeiro App Django.")

#Para que essa view seja acessível, o arquivo urls do PROJETO precisa ter o include
#Ele aponta para a URL do APP
#E a URL do APP aponta para View que irá lidar com a requisição!