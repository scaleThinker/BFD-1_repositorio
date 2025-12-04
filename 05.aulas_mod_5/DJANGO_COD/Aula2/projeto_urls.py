from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    #Lembre-se de incluir a rota para o seu app aqui!
    path('app/', include('myapp.urls')), 
]