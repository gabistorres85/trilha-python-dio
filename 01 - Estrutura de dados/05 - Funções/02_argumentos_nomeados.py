# Argumento nomeado é aquele que você passa chave e valor 
# é mais seguro para programar


def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# independe da ordem dos argumentos 
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# argumento como dicionário, os ** (prepara o interpretador para receber o dicionário)
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
