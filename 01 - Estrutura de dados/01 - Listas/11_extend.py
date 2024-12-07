''' Diferente do append, é possível acrescentar mais de 1 elemento, 
no argumento passar a lista que deseja incluirn a lista original.
Sendo que essa lista não será uma linha alinhada, os elementos serão
acrecidos ao final da lista inicial'''

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
