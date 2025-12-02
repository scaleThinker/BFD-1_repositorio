"""
URL configuration for intro_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Não esqueça de adicionar a importação do include!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app_um/", include("app_um.urls")), 
    #lembre-se de substituir o caminho e o nome do app!
    #O caminho adicionado aqui será uma url que apontará para o app:
    #Exemplo: 127.0.0.1:8000/meu_app
    #E irá incluir as URLs contidas em nome_do_app.urls
]
