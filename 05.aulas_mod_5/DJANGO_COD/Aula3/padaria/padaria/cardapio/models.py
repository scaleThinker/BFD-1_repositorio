from django.db import models

# Create your models here.

class Produto(models.Model): #Lembre-se que essa herança é fundamental!
    """
    Este código é ligeiramente diferente do da aula 2, ok?
    """
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank = True)

    def __str__(self):
        return self.nome