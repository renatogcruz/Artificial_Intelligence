"""
curso: algoritmos geneticos em python
plataforma: udemy
sobre: Construa passo a passo um algoritmo de Inteligência 
       Artificial aplicado no cenário de transporte de produtos!
"""

class Produto():
	def __init__(self, nome, espaco, valor):
		self.nome = nome
		self.espaco = espaco
		self.valor = valor

if __name__ == '__main__':
	#p1 = Produto("Iphone 6", 0.0000899, 2199.12)
	lista_produtos = []
	lista_produtos.append(Produto("Geladeira dako", 0.751, 999.90))
	lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
	lista_produtos.append(Produto("TV 55", 0.400, 4345.99))
	lista_produtos.append(Produto("TV 42", 0.200, 2999.00))
	lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
	lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
	lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
	lista_produtos.append(Produto("Microondas Eletrolux", 0.0496, 308.66))
	lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
	lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
	lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.00))

	for produto in lista_produtos:
		print(produto.nome)





