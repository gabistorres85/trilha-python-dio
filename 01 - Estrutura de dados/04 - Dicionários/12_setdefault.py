# recebe 2 argumentos(chave, valor)
# Realiza uma busca no dicionário da chave declarada no argument
# se existir: retorna o valor já atribuído do cicionário, sem alterar 
# se não existir: acrescente a chave e o valor atribuído ao dicionário

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
