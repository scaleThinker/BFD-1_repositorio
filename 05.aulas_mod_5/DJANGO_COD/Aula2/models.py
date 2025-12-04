from django.db import models

#Create your models here

class Produto(models.Model): #Lembre-se que essa herança é fundamental!
    """
    Esta classe irá criar uma tabela Produto no banco de dados com os campos
    nome
    preco
    disponivel
    """
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    #Método de representação preferido para facilitar a visualização no shell e admin
    def __str__(self):
        return self.nome
    

#Lembre-se:

#Depois de modificar este arquivo você precisa executar os dois comandos de terminal que aplicam alterações.

#python manage.py makemigrations nome_do_app

#python manage.py migrate