# Descobrir o tipo do dado informado

a=str(input('Digite algo:'))

print('Só tem espaços?', a.isspace())
print('É um números?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em MAIÚSCULO?', a.isupper())
print('Está em minúsculo?', a.islower())
print ('Está Capitalizada?', a.istitle())

