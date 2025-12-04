from django.urls import path
from . import views

urlpatterns = [
    #caminho ficará assim: http://127.0.0.1:8000/seuapp/index
    path("index/", views.index,name="Index"),

    #Mapeia a URL 'itens/' para a view 'listar_itens'
    path("itens/", views.listar_produtos, name="lista_produtos"),
    #caminho ficará assim: http://127.0.0.1:8000/seuapp/itens
]