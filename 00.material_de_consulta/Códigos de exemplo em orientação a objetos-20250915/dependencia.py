"""
É um relacionamento no qual um elemento, depende de outro elemento,para sua especificação ou implementação.
A implicação mais importante é:
Se a definição da classe utilizada mudar, a classe que a utiliza pode ser afetada e precisar de alterações.
É considerada a forma mais fraca de relacionamento entre classes porque não implica um vínculo estrutural e permanente entre os objetos. 
Diferente da Associação (Agregação/Composição), onde um objeto guarda uma referência a outro como um atributo (self.outro_objeto).
Na Dependência, o vínculo é tipicamente temporário e localizado.
"""


class Ficha:
    def __init__(self, texto):
        self.conteudo = texto

class Impressora:
    def imprimir(self,documento): #A Impressora "usa um" Documento
        print(f"Imprimindo: {documento.conteudo}")

#Instanciações
imp_seg_andar = Impressora()
ficha_1 = Ficha("Qualquer texto")

#Execução
imp_seg_andar.imprimir(ficha_1)

#A impressora pode imprimir qualquer outro documento desde que ela contenha um atributo "conteudo"
#Após esse uso pontual, não existe mais nenhuma relação entre as duas classes.