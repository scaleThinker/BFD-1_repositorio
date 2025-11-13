#Neste arquivo implementaremos nossa fábrica simples (Simple Factory)
#É de suma importância que a Fábrica conheça as classes que irá utilizar.
from pagamentos import GatewayPix, GatewayCartaoCredito

class PagamentoFactory:
    """
    Esta é a nossa fábrica. Ela tem um único método
    responsável por centralizar a lógica de criação.
    Normalmente quando ela tem apenas um método, chamam de "Simple Factory"
    """
    
    def criar_gateway(self, tipo_pagamento):
        """
        Recebe uma string (ex: 'pix') e retorna o objeto
        do gateway correspondente.
        """
        if tipo_pagamento == 'pix':
            return GatewayPix()
        
        elif tipo_pagamento == 'cartao':
            return GatewayCartaoCredito()
        
        else:
            #Vamos levantar um erro se não é um método conhecido.
            raise ValueError(f"Tipo de pagamento '{tipo_pagamento}' não suportado.")
            

#Vale lembrar de if, elif e else devem ser evitados caso cresçam em volume!
#No factory method vamos falar sobre isso!
