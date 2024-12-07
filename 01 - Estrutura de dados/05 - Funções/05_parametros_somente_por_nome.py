# PARÂMETROS PODE SEM POSICIONAIS, NOMEADOS OU HIBRIDOS
# Para definir uma forma obrigatória de parâmetro:
# / - todos os anteriores a ela são declarados apenas por posição 
# * - todos os parâmetros após a ele são nomeados

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
