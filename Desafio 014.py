# Conversor de temperaturas

# Convertendo de Celcius para Fahrenheit e Kelvin
c = float(input('Digite uma temperatura em Celcius: ') )
f = c * 9 / 5 + 32
k = c + 273.15 
print(f'A temperatura de {c:.2f}° Celcius é igual a {f:.2f}° em Fahrenheit e a {k:.2f}° em Kelvin')

# Convertendo de Fahrenheit para Celcius e Kelvin
f1 = float(input('Digite uma temperatura em Fahrenheit: '))
c1 = (f1 - 32) * 5 / 9
k1 = c1 + 273.15
print(f'A temperatura de {f1:.2f}° Fahrenheit é igual a {c1:.2f}° Celcius e {k1:.2f}° em Kelvin')

# Convertendo de Kelvin para Celcius e Fahrenheit
k2 = float(input('Digite uma temperatura em Kelvin: '))
c2 = k2 - 273.15
f2 = c2 * 9 /5 + 32
print(f'A temperatura de {k2:.2f}° Kelvin é igual a {c2:.2f}° Celcius e {f2:.2f}° em Fahrenheit')