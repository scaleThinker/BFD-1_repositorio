"""
3 relacionamentos principais:
- Associação (Agregação e Composição);
- Herança;
- Dependência.
"""
"""
class Livro:
    def __init__(self, autor):
        self.autor = autor
        self.cap = []

    def adicionar_cap(self,capitulo):
        self.cap.append(capitulo)
        print(f"'{capitulo.texto}' foi adicionado ao livro.")

    def exibircap(self):
        for capitulo in self.cap:
            capitulo.exibir_txt()
            

class Capitulo:
    def __init__(self, texto):
        self.texto = texto

    def exibir_txt(self):
        print (f"{self.texto}")


livr = Livro("Mauricio de Abreu")

cap = Capitulo("Texto capítulo 1")
cap2 = Capitulo("Texto capítulo 2")
cap3 = Capitulo("Texto capítulo 3")
livr.adicionar_cap(cap)
livr.adicionar_cap(cap2)
livr.adicionar_cap(cap3)
livr.exibircap()
"""

# Crie 4 classes: Computador, Memoria, Placa_mae, SSD.
# Ao iniciar um computador faz sentido que todos os seus componentes iniciem juntos.
# Se algum deles não for iniciado encontraremos erros, da mesma forma que não faz sentido
# iniciar esses componentes de forma isolada.
# Produza um classe Computador composta pelas classes Memoria, Placa_mae e SSD

class Memoria:
    def __init__(self):
        self.status = False
    
    def usar_memoria(self):
        self.status = True
        return self.status

class Placa_mae:
    def __init__(self):
        self.status = False
    
    def usar_placa(self):
        self.status = True
        return self.status 
    
class SSD:
    def __init__(self):
        self.status = False
    
    def usar_ssd(self):
        self.status = True
        return self.status 

class Computador:
    def __init__(self):
        self.status = False
        self.memoria = Memoria()
        self.placa_mae = Placa_mae()
        self.ssd = SSD()

    def ligar_comp(self):
        self.memoria.usar_memoria()
        self.placa_mae.usar_placa()
        self.ssd.usar_ssd()
        
        if self.memoria.status == True and self.placa_mae.status == True and self.ssd.status == True:
            print(f"O computador foi ligado com sucesso")
            self.status = True
            return self.status 
        else:
            print(f"O computador não foi ligado, verificar Hardware")
            return self.status 

pc1 = Computador()
pc1.ligar_comp()