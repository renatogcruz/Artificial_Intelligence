"""
# Deve ficar dessa maneira, para que o usuário adicione quantas variáveis ele quiser

inputsDef = [{ "name": "input1", "type": "continuous", "range": [0,10]},
			 { "name": "input1", "type": "continuous", "range": [0,10]}
			 ]

"""
		
import random 

dic = {"name": "largura", "min": 1, "max": 10}

#print(dic["name"])
#print(dic["min"])
#print(type(dic["min"]))
#print(dic["max"])
#print(type(dic["max"]))

if (type(dic["min"]) == float) and (type(dic["max"]) == float):
	print(type(dic["min"]))
	print(random.uniform(dic["min"], dic["max"])) #para flot
else:
	print(type(dic["min"]))
	print(random.randint(dic["min"], dic["max"])) #para int


#print(random.randint(dic["min"], dic["max"])) #para int
#print(random.uniform(dic["min"], dic["max"])) #para flot

#for i in range(dic["range"][1]):
#	print(i)
