"""
3 relacionamentos principais:
- Associação (Agregação e Composição);
- Herança;
- Dependência.
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

cap = Capitulo("bla")
cap2 = Capitulo("XY")
livr.adicionar_cap(cap2)
livr.adicionar_cap(cap)
livr.exibircap()



