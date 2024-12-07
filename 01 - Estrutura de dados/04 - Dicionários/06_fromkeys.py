# Método para criar chaves
# Cria chaves e atribui none como valor
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)
# ao colocar o segundo argumento, padroniza um valor para as chaves criadas.
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
