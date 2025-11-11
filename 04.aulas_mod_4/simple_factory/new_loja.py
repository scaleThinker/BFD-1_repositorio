# AGORA, a loja SÓ precisa conhecer a FÁBRICA
from fabrica import PagamentoFactory

def finalizar_compra(gateway, valor):
    """Esta função não mudou nada. Ela já era desacoplada."""
    print(f"\nFinalizando compra de R$ {valor:.2f}")
    resultado = gateway.processar_pagamento(valor)
    print(f"Resultado: {resultado}")


# --- NOSSO NOVO CÓDIGO PRINCIPAL ---

#1. Criamos UMA instância da fábrica
fabrica = PagamentoFactory()

#2. Simulamos uma escolha do usuário (poderia vir de uma rota Flask)
tipo_escolhido_1 = "pix"
valor_1 = 150.75

tipo_escolhido_2 = "cartao"
valor_2 = 80.20

try:
    #3. Pedimos à FÁBRICA para criar o objeto
    #A loja NÃO SABE qual objeto será. Só sabe que
    #ele assina o contrato 'BaseGatewayPagamento'.
    gateway_1 = fabrica.criar_gateway(tipo_escolhido_1)
    finalizar_compra(gateway_1, valor_1)

    gateway_2 = fabrica.criar_gateway(tipo_escolhido_2)
    finalizar_compra(gateway_2, valor_2)
    
    #Teste de erro
    tipo_escolhido_3 = "boleto"
    gateway_3 = fabrica.criar_gateway(tipo_escolhido_3)
    finalizar_compra(gateway_3, 100.00)

except ValueError as e:
    print(f"\nERRO AO PROCESSAR COMPRA: {e}")

"""
    Note que não existe uma grande diferença estrutural entre a implementação da aula passada 
    e de uma fábrica simples. A diferença reside no fato de que escondemos a criação de objetos 
    em outro arquivo, isolando a lógica. loja.py agora não mais vê GatewayPix!
"""
