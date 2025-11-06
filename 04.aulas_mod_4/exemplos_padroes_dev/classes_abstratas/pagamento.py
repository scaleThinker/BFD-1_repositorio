'''Resolução do exercicio. Arquivo 1'''
from abc import ABC, abstractmethod

class BaseGatewayPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor_total):
        pass

class GatewayPix(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via PIX. \n Gerando QR Code...")
        return True

class GatewayCartaoCredito(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via Cartão de Crédito. \n Conectando à operadora...")

class GatewayCartaoDebito(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via Cartão de Débito. \n Conectando à operadora...")


