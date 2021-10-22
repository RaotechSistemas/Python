# Quebrando um número

real=float(input('Digite um número real qualquer: '))
resp = int(real // 2)
rest = int(real % 2)
print(f'A porção inteira do número {real:.2f} é igual a: {resp} \nE seu resto é: {rest}')
if rest == 0:
    print(f'O número {real} é PAR!')
else:
    print(f'O número {real} é IMPAR!')    
