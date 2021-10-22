# Calculadora de Descontos

p = float(input('Digite o valor antigo do produto: '))
d = float(input('Qual a porcentagem do desconto?: '))
desc = p * (d / 100)
np = p - desc
print(f'O produto que custava R$ {p}, com desconto de {d}%, passa a custar R$ {np}.')