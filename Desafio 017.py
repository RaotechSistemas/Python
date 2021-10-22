# Catetos e Hipotenusa

'''
co = float(input('Indique o valor do cateto oposto: '))
ca = float(input('Indique o valor do cateto adjascente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('REGRA: O quadrado da hipotenusa é igual à soma dos quadrados dos catetos')
print(f'A hipotenusa vai medir: {h:.2f}.')
'''

# com importação da classe math

import math

co = float(input('Indique o valor do cateto oposto: '))
ca = float(input('Indique o valor do cateto adjascente: '))
h = math.hypot(co,ca)
print(f'A hipotenusa vai medir: {h:.2f}.')