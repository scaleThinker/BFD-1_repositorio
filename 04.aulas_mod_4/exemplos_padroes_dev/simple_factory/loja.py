from pagamentos import GatewayPix, GatewayCartaoCredito

def finalizar_compra(gateway, valor):
    #Nossa função polimórfica
    gateway.processar_pagamento(valor)

#Aqui ainda podemos fazer uma implementação melhor!
#O nosso código principal (loja.py) AINDA PRECISA saber
#que a classe 'GatewayPix' existe.
gateway_pix = GatewayPix() #Já que ela está sendo instanciada aqui
finalizar_compra(gateway_pix, 150.75)

#Consequentemente também precisa saber que 'GatewayCartaoCredito' existe.
gateway_cartao = GatewayCartaoCredito()
finalizar_compra(gateway_cartao, 80.20)


"""
    Note que este arquivo (loja.py) ainda contém uma implementação acoplada das classes concretas
    GatewayPix() e GatewayCartaoCredito(), já que elas estão sendo instanciadas diretamente no código
    Ainda que elas estejam assinando o contrato criado no arquivo "pagamentos.py"
    Se criarmos um GatewayBoleto, teremos que importá-lo e seguir o mesmo caminho das duas últimas implementações.


    Para solucionar o "problema" vamos criar um Fábrica Simples (Simple Factory).
    loja.py não vai mais falar com o GatewayPix diretamente.
    Ela vai falar com a fábrica e pedir um gateway do tipo pix, boleto, ou outro método de pagamento disponível.
    
"""
