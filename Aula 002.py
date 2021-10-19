'''
Crie um Script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

'''

d = input('Digite o dia (de 01 a 31): ')
m = input ('Digite o mês (de 01 a 12): ')
a = input ('Digite o ano (com 4 digitos): ')
    
print ('{}/{}/{}'.format(d,m,a))