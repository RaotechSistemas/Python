'''

Exercicios sobre Estruturação de Dados em Python

'''
# FUNÇÃO MAP() 
'''
# A função map() é utilizada para aplicar uma determinada função em cada item de um objeto iterável. Para que essa transformação seja feita, a função map() exige que sejam passados dois parâmetros: a função e o objeto iterável.

'''

# Exemplo 1
print("Exemplo 1")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens) 

# função map() para transformar cada palavra da lista em letras minúsculas
# como o primeiro parâmetro da função map() precisa ser uma função, optamos por usar uma função lambda.

print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista) 

# A função map() retorna um objeto iterável. Para que possamos ver o resultado, precisamos transformar esse objeto em uma lista, aplicando o construtor list() para fazer a conversão

print(f"Agora sim, a nova lista é = {nova_lista}")


# Exemplo 2
print("\n\nExemplo 2")
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x*x, numeros))

# usando a função lambda (x) elevamos cada número da lista a ele mesmo (x*x) (quadrado de um número) e já fizemos a conversão do resultado da função map() para o tipo list.

print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")