# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Parametro():
    """No Grasshopper, todo paamêtro tem 1 nome e 1 valor (min até um max)"""
    def __init__(self, nome, minimo, maximo):    #o valor entra nesse algoritmo
        self.nome = nome                         #parametro nome. Ex.: largura
        self.minimo = minimo                     #parametro min. Ex.: 1
        self.maximo = maximo
    
if __name__ == '__main__':
    lista_parametros = []
    lista_parametros.append(Parametro('Altura', 1, 5))
    lista_parametros.append(Parametro('Largura', 6, 10))
    lista_parametros.append(Parametro('Profundidade', 11, 20))
    for parametro in lista_parametros:
        print(parametro.nome)
