'''
Objeto de primeira classe:
1. Pode ser usado como argumento
2. Pode ser usado como retorno
3. Pode ser atribuído a uma variável

** Funções podem ser objetos de primeira classe
'''
def somar(a, b):
    return a + b

# Um ex de uso de função como argumento 
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
