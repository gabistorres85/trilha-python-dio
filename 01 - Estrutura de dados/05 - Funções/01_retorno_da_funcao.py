# possivel retornar mais de um valor
# se não tiver um retorno definido, por padrão retorna None


def calcular_total(numeros):
    return sum(numeros)

# exemplo com retorno de dois valores 
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # retorna uma tubla! 


def func_3():
    print ("ola mundo") 

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print (func_3) # retorna none