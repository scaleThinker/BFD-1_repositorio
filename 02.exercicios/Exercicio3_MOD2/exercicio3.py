# 1 - No contexto de modelagem de jogos, crie uma classe Player. Ela deve obedecer as seguintes condições.
# A - Os parâmetros de inicialização do objeto devem ser: nome, vida, mana.
# B - Os atributos vida e mana precisam ser privados.
# C - A classe deve conter métodos que retornem os atributos privados.
# D - A classe deve ter dois métodos públicos: sofrer_dano e usar_magia. 
# Sofrer dano causará dano a vida do player, usar magia diminuirá a mana. É preciso garantir que ambos os atributos não sejam menores do que 0.
# E - A classe deve ter um atributo público chamado "morto", se a vida chegar a 0, esse atributo deve ser modificado para verdadeiro.

import time

class Player:
    def __init__(self,nome,vida=100,mana=100):
        self.nome = nome
        self._vida = vida
        self._mana = mana
        self.morto = False
    
    def status_vida(self):
        return self._vida

    def status_mana(self):
        return self._mana
    
    def sofrer_dano(self,dano):
        if not self.morto:
            self._vida -= dano

            if self._vida < 0:
                self._vida = 0
            
            print (f"{self.nome} sofreu {dano} de dano. Vida restante: {self._vida}")
            
            if self._vida == 0:
               self.morto = True
               print(f"{self.nome} foi derrotado!")

    def usar_magia(self,custo_mana):
        if not self.morto and self._mana > custo_mana:
            self._mana -= custo_mana
            print(f"{self.nome} usou magia. Mana restante: {self._mana:.2f}")
            return True
        elif self.morto:
            print(f"{self.nome} está morto e não pode usar magia.")
            return False
        else:
            print(f"{self.nome} não tem mana suficiente para a magia.")
            return False
        
# 2 - Utilizando a classe Player produzida no exercício 1, faça o seguinte:
# A - Crie 3 classes filhas: Mago, Guerreiro, Arqueiro.
# B - Cada subclasse deve utilizar o inicializador da classe mãe (super().__init__) e adicionar mais 1 atributo específico a cada subclasse, sendo eles: 
# Mago -> elemento.
# Guerreiro -> constituicao.
# Arqueiro -> alcance_de_visao.
# C - As subclasses Mago e Guerreiro devem ter 2 métodos polimórficos:
# A classe Mago terá um método usar_magia (atenção ao conceito de polimorfismo) que gastará sempre 15% a menos de mana.
# A classe Guerreiro deverá ter um método sofrer_dano, onde o atributo "constituicao" será o valor em % de redução de dano que o guerreiro receberia. Exemplo: se constituicao = 25, o guerreiro deve receber menos 25% de dano na vida.
# D- A classe Arqueiro deve ter 2 métodos: disparar_flechas e recarregar_aljava. Ao disparar flechas o arqueiro deve gastar 1% de sua mana por flecha, o máximo de disparos consecutivos deve ser 10. Ao ficar sem flechas ele deve recarregar a aljava, durante este tempo ele deve ficar proibido de disparar por 5 segundos. 
# E - A classe Mago deve ter um método chamado magia_elemental, ele deve consumir 50% da mana atual do mago, e 10% da vida atual.
# F - A classe Guerreiro deve ter um método chamado furia, onde ela consome 10% da vida atual do guerreiro (deve desconsiderar a redução de dano do guerreiro, ou seja, deve ser aplicada direto na vida).
# Sinta-se a vontade para criar atributos nas classes que possam te ajudar a implementar a solução.

class Mago(Player):
    def __init__(self,nome,_vida,_mana,elemento):
        super().__init__(nome,_vida,_mana)
        self.elemento = elemento

    def usar_magia(self,custo_mana):
        custo_total = custo_mana * 0.85
        return super().usar_magia(custo_total)

    def magia_elemental(self):
        if self.morto:
            print(f"{self.nome} está morto.")
            return False
        custo_mana = self._mana * 0.5
        custo_vida = self._vida * 0.1
        
        if self._mana >= custo_mana and self._vida >= custo_vida:
            self._mana -= custo_mana
            self._vida -= custo_vida
            print(f"{self.nome} lançou magia elemental de {self.elemento}")
            return True
        else:
            print(f"{self.nome} não tem recusor suficientes para lançar magia elemental.")
            return False
        
        
class Guerreiro(Player):
    def __init__(self,nome,_vida,_mana,constituicao):
        super().__init__(nome,_vida,_mana)
        self.constituicao = constituicao

    def sofrer_dano(self, dano):
        dano_final = dano * (1 - self.constituicao / 100)
        super().sofrer_dano(dano_final)
# F - A classe Guerreiro deve ter um método chamado furia, onde ela consome 10% da vida atual do guerreiro 
# (deve desconsiderar a redução de dano do guerreiro, ou seja, deve ser aplicada direto na vida).    
    def furia(self):
        custo_vida = self.status_vida() * 0.1
        if self.status_vida() > custo_vida:
            self._vida -= custo_vida
            print(f"{self.nome} entrou em fúria. Fúria custou {custo_vida:.2f} de pontos de vida. Vida restante:{self._vida}.")
            return True
        else:
            print(f"{self.nome} está com pouca vida para usar fúria!")
            return False  

# D- A classe Arqueiro deve ter 2 métodos: disparar_flechas e recarregar_aljava. 
# Ao disparar flechas o arqueiro deve gastar 1% de sua mana por flecha, 
# o máximo de disparos consecutivos deve ser 10. Ao ficar sem flechas ele deve recarregar a aljava, 
# durante este tempo ele deve ficar proibido de disparar por 5 segundos. 
class Arqueiro(Player):
    def __init__(self,nome,_vida,_mana,alcance_de_visao):
        super().__init__(nome,_vida,_mana)
        self.alcance_de_visao = alcance_de_visao
        self.permissao = True
        self.disparos = 0

    def disparar_flechas(self):
        if not self.permissao:
            print (f"{self.name} está carregando e não pode disparar no momento.")
            return False
    
        if self.disparos < 10:
            custo_mana = self.status_mana() * 0.01
            if super().usar_magia(custo_mana):
                self.disparos += 1
            else:
                self.recarregar_aljava()
        else:
            print(f"Limite de disparos por {self.nome} atingido. Recarregando aljava.")
            self.recarregar_aljava()
    
    def recarregar_aljava(self):
        print(f"Recarregando aljava. Aguarde 5 segundos.")
        self.permissao = False
        time.sleep(5)
        self.disparos = 0
        self.permissao = True     
        print(f"Aljava recarregada!")
        
guerreiro = Guerreiro("Herold",200,50,25)
mago = Mago("Astrid",100,200,"Fogo")
arqueiro = Arqueiro("Somalia",90,100,150)

# guerreiro.sofrer_dano(50)
# guerreiro.furia()
# print(f"Vida atual de {guerreiro.nome}: {guerreiro.status_vida}")

# mago.magia_elemental()
# print(f"Vida atual de {mago.nome}: {mago.status_vida}")
# print(f"Mana atual de {mago.nome}: {mago.status_mana}")

for i in range (12):
    arqueiro.disparar_flechas()
    time.sleep(0.5)
arqueiro.disparar_flechas()