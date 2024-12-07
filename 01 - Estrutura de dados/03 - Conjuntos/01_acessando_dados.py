'''
Conjuntos não asceitam indexação, para consultar o valor 
primeiro deve ser transformado em lista.
'''
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
