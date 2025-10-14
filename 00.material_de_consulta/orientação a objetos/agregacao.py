"""
Até agora, criamos classes que funcionam bem de forma isolada.
No mundo real, porém, os sistemas são feitos de partes que colaboram. 

O relacionamento de agregação ("tem-um") é materializado através de atributos.
A classe agregadora pode conter atributos que são referências para objetos agregados¹;

É uma relação de agregação, vamos ao exemplo:
"""

#Classe Parte: Pode existir sozinha
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}")


#Classe Todo: Agrega objetos da classe Produto
class Carrinho:
    def __init__(self):
        self.produtos = [] #Uma lista para guardar os objetos Produto
                            #¹nota que nesta etapa poderiamos ter atributos da classe agregadora
                            #¹que apontam para objetos que serão agregados.

    #Este método RECEBE um objeto da classe Produto
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"'{produto.nome}' foi adicionado ao carrinho.")

    def calcular_total(self):
        total = 0.0
        #Iteramos sobre os OBJETOS Produto na lista
        for produto in self.produtos:
            total += produto.preco #Acessamos o atributo de outro objeto!
        return total

    def listar_produtos(self):
        print("\n--- Produtos no Carrinho ---")
        if not self.produtos:
            print("O carrinho está vazio.")
            return
        for produto in self.produtos:
            produto.exibir() #Chamamos o método de outro objeto!

#Criamos os objetos Produto (eles existem independentemente)
p1 = Produto("Placa de Vídeo RTX 5090", 9500.00)
p2 = Produto("Processador Intel i9", 3200.00)
p3 = Produto("Memória RAM 16GB", 450.00)

#Criamos o objeto Carrinho
meu_carrinho = Carrinho()

#O Carrinho INTERAGE com os Produtos, adicionando-os
meu_carrinho.adicionar_produto(p1)
meu_carrinho.adicionar_produto(p2)
meu_carrinho.adicionar_produto(p3)

#O Carrinho lista os produtos e calcula o total
meu_carrinho.listar_produtos()
total_da_compra = meu_carrinho.calcular_total()

print(f"\nTotal da compra: R$ {total_da_compra:.2f}")


#Após ver este exemplo, pense nas seguintes questões:
#O que acontece se uma classe tentar interagir com um atributo privado de outra classe?
#Qual seria o próximo passo dessa lógica? Alguma outra classe poderia utilizar informações do carrinho?