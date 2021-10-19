'''

Exercicios sobre Estruturação de Dados em Python

'''

# List Comprehension
# A listcomp é uma forma pythônica de escrever um for
'''

#Exemplo sem FOR

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = 'Python Java JavaScript C C# C++ Swift Go Kotlin'.split() # Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)

'''
#Exemplo com FOR 

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()
    
print("\nDepois da listcomp = ", linguagens)