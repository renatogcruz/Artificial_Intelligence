from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    cidade1 = Cidade('Cidade 1')
    cidade2 = Cidade('Cidade 2')
    cidade3 = Cidade('Cidade 3')
    cidade4 = Cidade('Cidade 4')
    cidade5 = Cidade('Cidade 5')
    cidade6 = Cidade('Cidade 6')
    cidade7 = Cidade('Cidade 7')
    cidade8 = Cidade('Cidade 8')
    cidade9 = Cidade('Cidade 9')
    cidade10 = Cidade('Cidade 10')
    cidade11 = Cidade('Cidade 11')
    cidade12 = Cidade('Cidade 12')
    cidade13 = Cidade('Cidade 13')
    cidade14 = Cidade('Cidade 14')
    cidade15 = Cidade('Cidade 15')
    cidade16 = Cidade('Cidade 16')
    
    cidade1.addCidadeAdjacente(Adjacente(cidade2))
    cidade1.addCidadeAdjacente(Adjacente(cidade3))
    cidade1.addCidadeAdjacente(Adjacente(cidade15))
    
    cidade2.addCidadeAdjacente(Adjacente(cidade1))
    cidade2.addCidadeAdjacente(Adjacente(cidade4))
    
    cidade3.addCidadeAdjacente(Adjacente(cidade1))
    cidade3.addCidadeAdjacente(Adjacente(cidade16))
    cidade3.addCidadeAdjacente(Adjacente(cidade12))
    
    cidade4.addCidadeAdjacente(Adjacente(cidade2))
    cidade4.addCidadeAdjacente(Adjacente(cidade5))
    cidade4.addCidadeAdjacente(Adjacente(cidade15))
    
    cidade5.addCidadeAdjacente(Adjacente(cidade4))
    cidade5.addCidadeAdjacente(Adjacente(cidade6))
    cidade5.addCidadeAdjacente(Adjacente(cidade15))
    
    cidade6.addCidadeAdjacente(Adjacente(cidade5))
    cidade6.addCidadeAdjacente(Adjacente(cidade7))
    cidade6.addCidadeAdjacente(Adjacente(cidade8))
    
    cidade7.addCidadeAdjacente(Adjacente(cidade6))
    cidade7.addCidadeAdjacente(Adjacente(cidade8))
    cidade7.addCidadeAdjacente(Adjacente(cidade9))
    cidade7.addCidadeAdjacente(Adjacente(cidade10))
    
    cidade8.addCidadeAdjacente(Adjacente(cidade6))
    cidade8.addCidadeAdjacente(Adjacente(cidade7))
    cidade8.addCidadeAdjacente(Adjacente(cidade11))
    
    cidade9.addCidadeAdjacente(Adjacente(cidade7))
    cidade9.addCidadeAdjacente(Adjacente(cidade11))
    
    cidade10.addCidadeAdjacente(Adjacente(cidade7))
    cidade10.addCidadeAdjacente(Adjacente(cidade13))
    
    cidade11.addCidadeAdjacente(Adjacente(cidade8))
    cidade11.addCidadeAdjacente(Adjacente(cidade9))
    cidade11.addCidadeAdjacente(Adjacente(cidade14))
    
    cidade12.addCidadeAdjacente(Adjacente(cidade3))
    cidade12.addCidadeAdjacente(Adjacente(cidade13))
    cidade12.addCidadeAdjacente(Adjacente(cidade14))
    
    cidade13.addCidadeAdjacente(Adjacente(cidade10))
    cidade13.addCidadeAdjacente(Adjacente(cidade12))
    
    cidade14.addCidadeAdjacente(Adjacente(cidade11))
    cidade14.addCidadeAdjacente(Adjacente(cidade12))
    cidade14.addCidadeAdjacente(Adjacente(cidade15))
    
    cidade15.addCidadeAdjacente(Adjacente(cidade1))
    cidade15.addCidadeAdjacente(Adjacente(cidade2))
    cidade15.addCidadeAdjacente(Adjacente(cidade5))
    cidade15.addCidadeAdjacente(Adjacente(cidade14))
    cidade15.addCidadeAdjacente(Adjacente(cidade16))
    
    cidade16.addCidadeAdjacente(Adjacente(cidade3))
    cidade16.addCidadeAdjacente(Adjacente(cidade15))
    

# testes
mapa = Mapa()

nome = mapa.cidade1.nome
print(nome)

visitado = mapa.cidade1.visitado
print(visitado)

adj = mapa.cidade1.adjacentes
print(adj)

for cidade in range(len(mapa.cidade1.adjacentes)):
    print(mapa.cidade1.adjacentes[cidade].cidade.nome)
    