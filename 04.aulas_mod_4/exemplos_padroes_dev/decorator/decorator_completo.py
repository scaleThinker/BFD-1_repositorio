#Agora nós já sabemos o que faz e como funciona um decorator!
#No entanto, nosso decorator tem algumas limitações!

#1 - Ele só funciona para funções que não recebem argumentos!
#2 - Ele "rouba" os metadados da função original como o nome e a docstring (se tiver) 

#Para implementar um decorator completo e adaptável a vários cenários
#Precisamos fazer um que aceite argumentos e preserve metadados

import functools
import time

def decorator_completo(funcao_original):
    """Decorator completo como deve ser implementado!"""

    #Vamos utilizar um decorator da biblioteca functools 
    #Ele permitirá a função ter seus dados preservados.
    @functools.wraps(funcao_original)
    def wrapper(*args, **kwargs): #Esta sintaxe diz ao python para aceitar qualquer quantidade de argumentos posicionais e nomeados!
        """Aqui vem a docsting do wrapper, está vai ser substituída!"""

        #vamos chamar nossa funcao_original repassando os argumentos!

        resultado = funcao_original(*args,**kwargs)

        return resultado #Note que agora retornamos o resultado da função original, como retorno da wrapper!
    return wrapper


#Feito nosso decorator, vamos testar com algo que contenha alguma lógica!

@decorator_completo
def somar(a,b) -> int:
    """Esta função soma dois números."""
    print("Executando a soma!!!")
    return a + b


#Agora que a função está decorada, vamos analisar sua chamada para ver o decorator em ação!

soma = somar(10,5)

print(f"Resultado da soma: {soma}")
print(f"\nNome da função: {somar.__name__}")
print(f"\nDocstring da função: {somar.__doc__}")

#Note que em ambientes de desenvolvimento a preservação do nome e docstring
#são fundamentais! Ser a preservação do nome a função chamaria wrapper!
