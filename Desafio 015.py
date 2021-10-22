# Aluguel de carros

k= (float(input('Total kilometragem percorrida: ')))
a= (int(input('Total de dias alugado: ')))
kr= (float(input('Valor por kilometro rodado: R$ ')))
ad = (float(input('Valor do dia de aluguel: R$ ')))
tk = k*kr # total de kilometros rodados
ta = a * ad # total dias de aluguel
total = tk + ta 
print(f'Total a pagar por {k:.2f} kilometros rodados  + {a} dias de aluguel: R$ {total:.2f}')