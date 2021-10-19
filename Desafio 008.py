# Converter metros em centimetros e milimetros
print('*' * 30)
m = float(input('Digite um valor em metros: '))
print('*' * 30)
cm = m * 100
mm = m * 1000

print(f'O valor de {m:.2f} metros corresponde a: \n {cm:.2f} centimetros \n {mm:.2f} milimetros')