# Calcular largura x Altura de uma parede e prever gasto com tinta (m2)

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
areaM2 = l*a
print(f'A área total da parede é de {areaM2}M².')
t= float(input('Qual o rendimento da tinta em M²/litro?: '))
rend = areaM2 / t
print(f'Sendo assim, uma parede com \n{a} metros de altura e \n{l} de largura, \ne sendo que a tinta escolhida rende \n{t} por M²/litro, serão necessarios \n{rend} litros de tinta para cobrir toda a área de {areaM2}.')