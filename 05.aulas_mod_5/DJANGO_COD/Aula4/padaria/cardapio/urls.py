from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #Exemplo: mapeia a URL base do App para a view 'index'

    path("cadastro/produto/",views.cadastro_produto, name="cadastro_produto"),

    path("cardapio", views.listar_produtos, name="cardapio")
]
