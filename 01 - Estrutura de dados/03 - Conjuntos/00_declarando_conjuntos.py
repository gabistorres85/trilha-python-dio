'''
Conjuto que não aceita duplicadas. 
Usos: representar conjuntos numéricos e retirar duplicadas de objetos iterávei
'''

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#forma de declarar pouco utilizada 
familia = {"Clarice", "Gabriel",'Gabriela','Yuri'}
print(familia)