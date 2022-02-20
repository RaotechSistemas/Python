import datetime as dt

#Calculadora que mostra em dias a diferença entre duas datas

print("\n===============Data inicial=============\n")


aa = int(input('----Digite o ano com 4 dígitos: '))
while aa < 1000:
    print(aa = int(input('----Digite o ano com 4 dígitos: ')))

mm = int(input('----Digite o mês, de 1 a 12: '))

if mm < 1 > 12:
    print(mm = int(input('---Digite o mês, de 1 a 12: ')))

dd = int(input('----Digite o dia: '))
if dd > 31:
    print("Digite um dia válido:")
    dd = int(input('----Digite o dia: '))

inicial = dt.date(aa, mm, dd)

print("\n===============Dias de Diferença=============\n")    

dias = int(input('----Digite a quantidade de dias: '))
while dias <= 0:
    print ("número inválido! Tente Novamente.")
    print(dias = int(input('----Digite a quantidade de dias: ')))
d= date(dias.day)
diferenca = inicial + d
resp = dt.date( diferenca)




print("Do dia ", inicial, " mais" , dias , " dias, chegará em " ,resp)



'''meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# Código que diz quantos dias a pessoa já viveu, com algumas condições e uso de lista

aa = int(input('----Digite o ano de seu nascimento: '))
while aa < 1000:
    print("Favor digite os quatro dígitos do ano.")
    aa = int(input('----Digite o ano de seu nascimento: '))
mm = int(input('01 - Janeiro\n02 - Fevereiro\n03 - Março\n04 - Abril\n05 - Maio\n06 - Junho\n07 - Julho\n08 - Agosto\n09 - Setembro\n10 - Outubro\n11 - Novembro\n12 - Dezembro\n ----Digite o mês de seu nascimento: '))

if mm != meses:
        print("Digite o número correspondente ao mês")
        mm = int(input('01 - Janeiro\n02 - Fevereiro\n03 - Março\n04 - Abril\n05 - Maio\n06 - Junho\n07 - Julho\n08 - Agosto\n09 - Setembro\n10 - Outubro\n11 - Novembro\n12 - Dezembro\n ----Digite o mês de seu nascimento: '))

dd = int(input('----Digite o dia de seu nascimento: '))
if dd > 31:
    print("Digite um dia válido:")
    dd = int(input('----Digite o dia de seu nascimento: '))
d = dt.date(aa, mm, dd)

tday = dt.date.today()
idade = tday - d
print(f"Você nasceu em ", d," e tem ", idade , "dias de vida.")'''




'''# Esse código mostra ano, mês, dia, hora, minuto e microssegundo do momento que é chamado

tday = dt.datetime.today() # Traz o dia atual
tdelta = dt.timedelta(hours=12) # Se hours = 12, dia de hoje; se hours = 24, dia de amanhã
print(f'Hoje é dia: ', tday + tdelta)'''


'''#Calculadora que mostra em dias a diferença entre duas datas

print("\n===============Data inicial=============\n")


aa = int(input('----Digite o ano com 4 dígitos: '))
while aa < 1000:
    print(aa = int(input('----Digite o ano com 4 dígitos: ')))

mm = int(input('----Digite o mês, de 1 a 12: '))

if mm < 1 > 12:
    print(mm = int(input('---Digite o mês, de 1 a 12: ')))

dd = int(input('----Digite o dia: '))
if dd > 31:
    print("Digite um dia válido:")
    dd = int(input('----Digite o dia: '))

print("\n===============Data Final=============\n")    

aaf = int(input('----Digite o ano com 4 dígitos: '))
while aaf < 1000:
    print(aaf = int(input('----Digite o ano com 4 dígitos: ')))

mmf = int(input('----Digite o mês, de 1 a 12: '))

if mmf < 1 > 12:
    print(mmf = int(input('---Digite o mês, de 1 a 12: ')))

ddf = int(input('----Digite o dia: '))
if ddf > 31:
    print("Digite um dia válido:")
    ddf = int(input('----Digite o dia: '))

inicial = dt.date(aa, mm, dd)
final = dt.date(aaf, mmf, ddf)


diferenca = final - inicial
print("Entre os dias ", inicial, " e " , final , " são " ,diferenca.days, " dias de diferença.")'''

'''dt_agora = dt.datetime.now() # informa a data atual
print(dt_agora.strftime('%B %d, %Y'))'''

'''dt_str = 'July 24, 2016'
dt = dt.datetime.strptime(dt_str, '%B %d, %Y') # Transforma uma data de String para DateTime
print(dt)

# strftime - Datetime para String
# strptime - String para Datetime'''