'''

Exercicios sobre Estruturação de Dados em Python

'''

# Lista

'''
vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

'''

'''
# Mesmo resultado.

vogais = [] # a lista começa vazia
print(f"Tipo do objeto vogais = {type(vogais)}") # indica que se trata de uma lista

vogais.append('a') # a instrução 'append' acrescenta o item à lista 'vogais':(posição '0', valor 'a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais): # a variavel 'p' quadra a posição e 'x' guarda o valor
    # a função enumerate() é usada para percorrer um objeto iterável retornando a posição e o valor
    print(f"Posição = {p}, valor = {x}")

'''    

lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

print("\nExemplos de slices:\n")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])
