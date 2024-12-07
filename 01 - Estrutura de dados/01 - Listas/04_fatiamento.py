# FATIAMENTO - seleciona parte da losta 

lista = ["p", "y", "t", "h", "o", "n"]

'''Lista [x:y:z] - x - inicio da fatia; y - final da fatia; z - step da fatia
inclui o x e exlui y
para declarar sem início e sem fim precisa colocar o step, nesse caso se for o padrão
irá trazer toda lista e se for -1 retorna a lista invertida
'''
print(lista[2:])  # ["t", "h", "o", "n"] 
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
