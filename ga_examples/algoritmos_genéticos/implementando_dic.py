"""
# Deve ficar dessa maneira, para que o usuário adicione quantas variáveis ele quiser

inputsDef = [{ "name": "input1", "type": "continuous", "range": [0,10]},
			 { "name": "input1", "type": "continuous", "range": [0,10]}
			 ]

"""
		
import random 

param1 = {"name": "largura", "min": 1.0, "max": 10.0}
param2 = {"name": "comprimento", "min": 4.0, "max": 8.0}

#print(param1["name"])
#print(param1["min"])
#print(type(param1["min"]))
#print(param1["max"])
#print(type(param1["max"]))

if (type(param1["min"]) == float) and (type(param1["max"]) == float):
	print("Este paramêtro é do tipo 'float'")
	print(random.uniform(param1["min"], param1["max"])) #para flot
else:
	print("Este paramêtro é do tipo 'inteiro'")
	print(random.randint(param1["min"], param1["max"])) #para int


#print(random.randint(dic["min"], dic["max"])) #para int
#print(random.uniform(dic["min"], dic["max"])) #para flot

#for i in range(dic["range"][1]):
#	print(i)
