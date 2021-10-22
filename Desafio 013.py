# Claculadora de aumentos

s = float(input('Digite o valor antigo do salário: '))
p = float(input('Qual a porcentagem do aumento?: '))
a = s * (p / 100)
ns = s + a
print(f'O salário que era de R$ {s:.2f}, com o aumento de {p:.2f}%, passa a ser de R$ {ns:.2f}.')