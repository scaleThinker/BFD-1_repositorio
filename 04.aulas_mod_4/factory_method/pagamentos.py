from abc import ABC, abstractmethod

#Nosso contrato:
class BaseGatewayPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor_total):
        pass

#Implementação do gateway pix
class GatewayPix(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via PIX. Gerando QR Code...")
        return {"status": "sucesso", "tipo": "pix"}

#Implementação do gateway cartão de crédito
class GatewayCartaoCredito(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via Cartão de Crédito. Conectando...")
        return {"status": "sucesso", "tipo": "cartao"}

class GatwayBoleto(BaseGatewayPagamento):
    def processar_pagamento(self, valor_total):
        print(f"Processando R$ {valor_total:.2f} via Boleto. Conectando...")
        return {"status": "sucesso", "tipo": "boleto"}           