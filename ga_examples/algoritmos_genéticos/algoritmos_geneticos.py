"""
curso: algoritmos geneticos em python
plataforma: udemy
sobre: Construa passo a passo um algoritmo de Inteligência 
       Artificial aplicado no cenário de transporte de produtos!
"""

from random import random

class Produto():
	def __init__(self, nome, espaco, valor):
		self.nome = nome
		self.espaco = espaco
		self.valor = valor

class Individuo():
	def __init__(self, espacos, valores, limite_espacos, geracao=0):
		self.espacos = espacos
		self.valores = valores
		self.limite_espacos = limite_espacos
		self.nota_avaliacao = 0
		self.espaco_usado = 0
		self.geracao = geracao
		self.cromossomo = []

		for i in range(len(espacos)):
			if random() < 0.5:
				self.cromossomo.append("0")
			else:
				self.cromossomo.append("1")

	def avaliacao(self):
		nota = 0
		soma_espacos = 0
		for i in range(len(self.cromossomo)):
			if self.cromossomo[i]  == "1":
				nota += self.valores[i]
				soma_espacos += self.espacos[i]
		if soma_espacos >self.limite_espacos:
			nota = 1
		self.nota_avaliacao = nota 
		self.espaco_usado = soma_espacos

	def crossover(self, outro_individuo):
		corte = round(random() * len(self.cromossomo))

		filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
		filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

		filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
		Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
		filho[0].cromossomo = filho1
		filho[1].cromossomo = filho2
		return filhos

	def mutacao(self, taxa_mutacao):
		print("Antes %s" % self.cromossomo)
		for i in range(len(self.cromossomo)):
			if random() < taxa_mutacao:
				if self.cromossomo[i] == "1":
					self.cromossomo[i] = "0"
				else:
					self.cromossomo[i] =="1"
		print("Depois %s " %self.cromossomo)
		return self




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

	#for produto in lista_produtos:
	#	print(produto.nome)

	espacos = []
	valores = []
	nomes = []
	for produto in lista_produtos:
		espacos.append(produto.espaco)
		valores.append(produto.valor)
		nomes.append(produto.nome)
	limite = 3 #podemos carregar três metros cubicos

	individuo1 = Individuo(espacos, valores, limite)
	#print("espaços = %s" % str (individuo1.espacos))
	#print("valores = %s" % str (individuo1.valores))
	#print("cromossomo = %s" % str (individuo1.cromossomo))
	print("\nIndivíduo 1")
	#print("\nComponente da carga")
	for i in range(len(lista_produtos)):
		if individuo1.cromossomo[i] == 1:
			print("Nome: %s R$ %s" % (lista_produtos[i].nome, lista_produtos[i].valor))

	individuo1.avaliacao()
	print("Nota = %s" % individuo1.nota_avaliacao)
	print("Espaço usado = %s" % individuo1.espaco_usado)

	individuo2 = Individuo(espacos, valores, limite)
	#print("espaços = %s" % str (individuo1.espacos))
	#print("valores = %s" % str (individuo1.valores))
	#print("cromossomo = %s" % str (individuo1.cromossomo))
	print("\nIndivíduo 2")
	#print("\nComponente da carga")
	for i in range(len(lista_produtos)):
		if individuo2.cromossomo[i] == 1:
			print("Nome: %s R$ %s" % (lista_produtos[i].nome, lista_produtos[i].valor))

	individuo2.avaliacao()
	print("Nota = %s" % individuo2.nota_avaliacao)
	print("Espaço usado = %s" % individuo2.espaco_usado)

	#individuo1.crossover(individuo2)

	individuo1.mutacao(0.05)
	individuo2.mutacao(0.05)

