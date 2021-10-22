# Criando uma tabuada
print('#'*30)
n = int(input('Digite um número: '))
print('#'*30)
print('[1] - Soma \n[2] - Subtração \n[3] - Multiplicação \n[4] - Divisão')
print('#'*30)
tab = int(input('Escolha sua tabuada: '))

if tab == 1:
    n1 = n+1
    n2 = n+2
    n3 = n+3
    n4 = n+4
    n5 = n+5
    n6 = n+6
    n7 = n+7
    n8 = n+8
    n9 = n+9
    n10 = n+10
    print(f'{n1} \n{n2} \n{n3} \n{n4} \n{n5} \n{n6} \n{n7} \n{n8} \n{n9} \n{n10}')
elif tab == 2:
    n1 = n-1
    n2 = n-2
    n3 = n-3
    n4 = n-4
    n5 = n-5
    n6 = n-6
    n7 = n-7
    n8 = n-8
    n9 = n-9
    n10 = n-10
    print(f'{n1} \n{n2} \n{n3} \n{n4} \n{n5} \n{n6} \n{n7} \n{n8} \n{n9} \n{n10}')

elif tab == 3:
    n1 = n*1
    n2 = n*2
    n3 = n*3
    n4 = n*4
    n5 = n*5
    n6 = n*6
    n7 = n*7
    n8 = n*8
    n9 = n*9
    n10 = n*10
    print(f'{n1} \n{n2} \n{n3} \n{n4} \n{n5} \n{n6} \n{n7} \n{n8} \n{n9} \n{n10}')

elif tab == 4:
    n1 = n/1
    n2 = n/2
    n3 = n/3
    n4 = n/4
    n5 = n/5
    n6 = n/6
    n7 = n/7
    n8 = n/8
    n9 = n/9
    n10 = n/10
    print(f'{n1} \n{n2} \n{n3} \n{n4} \n{n5} \n{n6} \n{n7} \n{n8} \n{n9} \n{n10}') 
else: 
    print('!'*30)
    print('Opção Inválida! Tente novamente.')