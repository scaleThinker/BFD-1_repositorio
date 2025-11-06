'''Resolução do exercicio. Arquivo 2'''
from pagamento import GatewayPix,GatewayCartaoCredito,GatewayCartaoDebito

def finalizar_compra(gatway, valor):
    gatway.processar_pagamento(valor)

gatway_pix = GatewayPix()
gatway_cartao = GatewayCartaoCredito()
gatway_debito = GatewayCartaoDebito()

finalizar_compra(gatway_pix, 150.75)
finalizar_compra(gatway_cartao, 80.20)
finalizar_compra(gatway_debito,55.99)
