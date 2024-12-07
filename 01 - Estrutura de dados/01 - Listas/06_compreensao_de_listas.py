"""COMPREENSÃO DE LISTA 
 criar uma lista nova com base em uma lista já existente (filtro)
 ou uma lista modificada com base nos elementos anteriores
 primeira parte é o retorno da função;
 segunda parte é o for
 terceira parte, que não é obrigatória o filtro
 """


# Filtrar lista
""" substitui:
numeros = [1, 30, 21, 2, 9, 65, 34]
numeros_pares =[]
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
"""
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
'''Substitui:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado =[]
for numero in numeros:
    quadrado.append(numero**2)
'''
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
