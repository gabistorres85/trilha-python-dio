# Esse método diferente do pop(), não receve o argumento e retira as chaves senquencialmente
# Gera exceção quando o dicionário está vazio

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
