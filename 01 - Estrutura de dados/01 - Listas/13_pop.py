''' Funcionamento padrão da lista é uma fila (FIFO)
por isso no append os elementos são inclusos no final da lista 
e o pop retira o último elemento da lista 
sendo que é possível passar como argumento o índex do elemento
a ser removido.'''

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
