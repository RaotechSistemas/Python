'''

Faça um prorama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

'''
algo = str(input('Digite algo: '))
print(type(algo))
print('Só tem espaços?:',algo.isspace())
print('É um número?:',algo.isnumeric())
print('É alfabetico?:',algo.isalpha())
print('É alfanumérico?:',algo.isalnum())
print('Está em MAIÚSCULA?:',algo.isupper())
print('Está em minúsculo?:',algo.islower())
print('Está Capitalizada?:',algo.istitle())