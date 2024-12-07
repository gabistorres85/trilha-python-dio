# Funções podem retornar mais de um valor 
# Torna o código mais legível
# Reaproveitamento de códigos
# Parâmetros de entrada 
# Funções está no paradigma de programaçao estruturada

# Definindo uma função que não recebe parâmetro 
def exibir_mensagem():
    print("Olá mundo!")

# Função com parâmetro
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Função com parâmetro pa'drão
# nesse caso é possível chamar a função sem parâmetro
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Como chamar a função:
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
