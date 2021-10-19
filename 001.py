'''

Exercicios sobre Estruturação de Dados em Python

'''

# Sequência

'''
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")
print(f"Mudando texto para MAIUSCULAS: {texto.upper()}")
print(f"Mudando texto para minúsculas: {texto.lower()}")
print(f"Mudando texto para Capitalizada: {texto.title()}")
print(F"Trocando a letra 'i' por 'x': {texto.replace('i', 'x')}")
print(f"Mostrar todo o texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n") # o comando \n faz saltar uma linha
palavras = texto.split()  # usada para "cortar" um texto e transformá-lo em uma lista
print(f"palavras = {palavras}") 
print(f"Tamanho de palavras = {len(palavras)}")

'''

# Exemplo de uso prático da função Estrutura de dados para análise de texto (análise de sentimentos em texto)

texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print(f"Tamanho do texto = {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"Quantidade de vezes que string ou strings aparecem = {total}")