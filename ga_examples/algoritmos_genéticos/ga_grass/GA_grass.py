# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import random, randint

class Parametro():
    """No Grasshopper, todo paamêtro tem 1 nome e 1 valor (min até um max)"""
    def __init__(self, nome, minimo, maximo):    #o valor entra nesse algoritmo
        self.nome = nome                         #parametro nome. Ex.: largura
        self.minimo = minimo                     #parametro min. Ex.: 1
        self.maximo = maximo
        

class Individuo():
    #o indíviduo é o próprio cromossomo (ex.: forma_objeto (2, 8, 15))
    def __init__(self, minimos, maximos, geracao=0):
        self.minimos = minimos
        self.maximos = maximos
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []                     #valores entre min e max dos parametros

        for i in range(len(lista_parametros)):   #escolher valores entre min e max aleatoriamente
            if (type(minimos[i]) == float) and (type(maximos[i]) == float):
                self.cromossomo.append(random.uniform(minimos[i], maximos[i])) #instance
            else:
                self.cromossomo.append(randint(minimos[i], maximos[i])) 
    
    def avaliacao(self):
        """Função fitness"""
        #receberá o valor_objetivo de cada individuo (virá do modelo) Por exemplo, relação área/volume
        nota =randint(1000, 2222) #função provisório para continuar o desenv. script
        self.nota_avaliacao = nota
    
    def crossover(self, outro_individuo):
        """Determina o ponto de crossover"""
        #corte = int(round(random()  * len(self.cromossomo))) #um número randômico (0 ou 1) vai multiplicar pelo tamanho do cromossomo (round é para arredondar)
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]  #o filho recebe parte do cromossomo (de 0 até corte) do outro indíviduo
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]  #o outro_ind é o individuo2 

        filhos = [Individuo(self.minimos, self.maximos, self.geracao + 1),
                  Individuo(self.minimos, self.maximos, self.geracao + 1)]
        filhos[0].cromossomo = filho1   #filho 1 e 2 na verdade está criando cromossomos
        filhos[1].cromossomo = filho2
        return filhos
    
if __name__ == '__main__':
    lista_parametros = []
    lista_parametros.append(Parametro('Altura', 1, 5))
    lista_parametros.append(Parametro('Largura', 6, 10))
    lista_parametros.append(Parametro('Profundidade', 11, 20))
    #for parametro in lista_parametros:
    #    print(parametro.nome)
    
    minimos = []
    maximos = []
    nomes = []
    for parametro in lista_parametros:
        minimos.append(parametro.minimo)
        maximos.append(parametro.maximo)
        nomes.append(parametro.nome)
    
    individuo1 = Individuo(minimos, maximos)
    print("\nIndivíduo 1")
    for i in range(len(lista_parametros)):
        print("Nome: %s" %(lista_parametros[i].nome))
       
    individuo1.avaliacao()
    print("Nota = %s" % individuo1.nota_avaliacao)
    
    individuo2 = Individuo(minimos, maximos)
    print("\nIndivíduo 2")
    for i in range(len(lista_parametros)):
        print("Nome: %s" %(lista_parametros[i].nome))
       
    individuo1.avaliacao()
    print("Nota = %s" % individuo2.nota_avaliacao)
    
    individuo1.crossover(individuo2)
    
