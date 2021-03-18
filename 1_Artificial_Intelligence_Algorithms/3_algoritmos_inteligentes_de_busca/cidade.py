class Cidade:
    def __init__(self, nome):    # construtor da nossa classe
        self.nome = nome         #criando atributo para esta classe
        self.visitado = False
        self.adjacentes = []     # lista de cidades adjacentes
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)
        
#c = Cidade('teste')
#print(c.nome)
#print(c.visitado)