# 3 - Suponha que você faz parte de uma equipe de desenvolvimento para softwares de astronomia e irá criar um protótipo expansível de sistema solar, 
# para isso siga as definições:
# A - Crie uma classe Planeta, ela deve ser inicializada com os parâmetros: nome, raio_equatorial, dist_sol e composicao.
# B - O raio_equatorial deve ser em km, a dist_sol em milhões de km e composição "Rochoso" ou "Gasoso".
# C - Adicione um método de apresentação, sem parâmetros, que mostre na tela as informações do planeta.
# D - Fora da classe, crie uma função que calcule e retorne o valor da distância do planeta instanciado até o SOL em UA (Unidades Astronômicas, 
# representada pela distância da terra até o Sol, aproximadamente 150 milhões de km). 
# Utilize a fórmula: dist_sol / 150. Essa função deve receber como parâmetro o atributo dist_sol da classe planeta, 
# ou seja, deve funcionar para qualquer objeto do tipo planeta.
# Pesquisa na internet pelas informações de 3 planetas e as utilize para instanciar 3 objetos. 
# Execute o método de apresentação e a função de distância para cada um dos objetos instanciados.

class Planeta:
    def __init__(self, nome, raio_equatorial, dist_sol, composicao):
        
        self.nome = nome
        self.raio_equatorial = raio_equatorial  
        self.dist_sol = dist_sol
        self.composicao = composicao
    
    def apresentacao(self):
        print(f"Planeta: {self.nome}")
        print(f"Raio Equatorial: {self.raio_equatorial:,.0f} km")
        print(f"Distância do Sol: {self.dist_sol:,.1f} milhões de km")
        print(f"Composição: {self.composicao}")


def calcular_distancia_ua(dist_sol):
    return dist_sol / 150

terra = Planeta("Terra", 6378, 149.6, "Rochoso")
marte = Planeta("Marte", 3396, 227.9, "Rochoso")
jupiter = Planeta("Júpiter", 71492, 778.5, "Gasoso")

terra.apresentacao()
print(f'Valor UA =', calcular_distancia_ua(terra.dist_sol))

marte.apresentacao()
print(f'Valor UA =', calcular_distancia_ua(marte.dist_sol))

jupiter.apresentacao()
print(f'Valor UA =', calcular_distancia_ua(jupiter.dist_sol))