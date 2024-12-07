'''
ESCOPO LOCAL E ESCOPO GLOBAL
1. Local: dentro do bloco da função
Ao fim do método, as alterações internas são perdidas.
Objetos multáveis se for chamado externamente receberam
a alteração realizada internamente no método.
2. Global: Fora da função
variável global: ela vem acompanhada pela palavra "global"
mesmo sem ser declarada no parâmetro as alterações 
sofridas no escopo local irão permanecer no escopo global. 
Deve ser usada com muito cuidado pois dificulta 
a manutenção do código.

'''

salario = 2000

'''
Se tentar utilizar uma variável do escopo global, 
dentro de uma função, sem solicitar nos parâmetros
o interpretador não resgata a variável. 
Uma forma de realizar isso sem declarar nos parâmetros
é declarar a variável como global
'''
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
