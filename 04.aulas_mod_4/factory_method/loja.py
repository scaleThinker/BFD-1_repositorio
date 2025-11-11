#Note que nosso arquivo loja.py agora só irá conter a importação das classes que irão fabricar objetos!

from creators import BaseGatewayCreator, PixCreator, CartaoCreator, BoletoCreator

#O cliente não precisa saber qual gateway existe.
#Ele só precisa saber qual 'Criador' ele quer.
def executar_compra_na_loja(creator: BaseGatewayCreator, valor: float):
    """
    Esta função representa o código cliente.
    Ela recebe um *Criador* e não se importa qual é.
    Essa implementação obedece o conceito de:
    'Aberto para extensão, fechado para modificação"
    """
    creator.processar_compra(valor)


# --- Simulação da Loja ---

#Cenário 1: O usuário escolheu pagar com PIX
#A loja instancia o criador de PIX
print("--- Cenário 1: Pagamento com PIX ---")
creator_pix = PixCreator()
executar_compra_na_loja(creator_pix, 150.75)


#Cenário 2: O usuário escolheu pagar com Cartão
#A loja instancia o criador de Cartão
print("\n--- Cenário 2: Pagamento com Cartão ---")
creator_cartao = CartaoCreator()
executar_compra_na_loja(creator_cartao, 80.20)

#Cenário 3: O usuário escolheu pagar com Boleto
print("\n--- Cenário 3: Pagamento com Boleto ---")
creator_boleto = BoletoCreator()
executar_compra_na_loja(creator_boleto, 1125.20)

"""
    Uma observação importante!
    Nos nossos exemplos simplificados, pode parecer que não existe diferença entre o simple factory
    e o factory method, no entanto, quando as classes tem implementações de lógicas complexas,
    implementar um fábrica facilitará seu uso, pois AS CLASSES ESPECIALISTAS vão lidar com as lógicas
    complexas, quem utilizará essas classes não precisará lidar com isso!

Para pensar essa observação: Como seria se GatewayPix precisasse de 6 parâmetros diferentes para ser criado?

"""
