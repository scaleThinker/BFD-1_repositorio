from abc import ABC, abstractmethod
from pagamentos import BaseGatewayPagamento, GatewayPix, GatewayCartaoCredito, GatwayBoleto

#Aqui temos a criação do nosso Criador Abstrato
#Ele será nossa classe resposável pela lógica de "contrato" como vinhamos aprendendo
class BaseGatewayCreator(ABC):
    """
    O Creator Abstrato declara o 'método de fábrica' (factory method)
    que deve retornar um objeto do tipo Produto (BaseGatewayPagamento).
    """
    
    @abstractmethod
    def criar_gateway(self) -> BaseGatewayPagamento: #Note que nosso Factory Method, aponta para o contrato!
        """Este é o Factory Method."""
        pass
    
    def processar_compra(self, valor) -> dict:
        """
        Este é um método de negócio. Ele NÃO sabe qual gateway
        está criando, ele apenas usa o factory method.
        """
        print(f"\nIniciando processamento de compra de R$ {valor:.2f}...")
        
        #1. Pega o gateway (deixando a subclasse decidir qual)
        gateway = self.criar_gateway()
        
        #2. Usa o gateway
        resultado = gateway.processar_pagamento(valor)
        #Note que podemos chamar processar_pagamento pois o contrato estabelecido
        #em pagamentos, força as classes a implementarem esse método!
        
        print(f"Processamento finalizado: {resultado}")
        return resultado


#CRIADOR CONCRETO 1
class PixCreator(BaseGatewayCreator): #A classe herda a classe responsável pela fábrica!
    """
    Esta subclasse implementa o factory method para criar
    e configurar um GatewayPix.
    """
    def criar_gateway(self) -> BaseGatewayPagamento:
        #Aqui poderia ter uma lógica complexa, como:
        #chave_pix = config.get('CHAVE_PIX_BANCO')
        #return GatewayPix(chave_pix)
        print("PixCreator: Criando Gateway de Pix.")
        return GatewayPix() #Criação do objeto GatewayPix() cuja classe original obedece o contrato no arquivo pagamentos!


#CRIADOR CONCRETO 2
class CartaoCreator(BaseGatewayCreator):
    """
    Esta subclasse implementa o factory method para criar
    e configurar um GatewayCartaoCredito.
    """
    def criar_gateway(self) -> BaseGatewayPagamento:
        #Aqui poderia ter outra lógica complexa:
        #chave_api = config.get('API_KEY_CARTAO')
        #return GatewayCartaoCredito(chave_api)
        print("CartaoCreator: Criando Gateway de Cartão.")
        return GatewayCartaoCredito()

class BoletoCreator(BaseGatewayCreator):
    def criar_gateway(self) -> BaseGatewayPagamento:
        print("BoletoCreator: Criando Gateway de Boleto.")
        return GatwayBoleto()