idade = int(input("Digite a sua idade: "))
while idade == (''): # LINHA COM ITEM VAZIO
    print("Digite um valor válido!")
    print(idade = int(input("Digite a sua idade: ")))



salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Erro ao preencher! Digite o seu salário[MAIOR QUE 0]: "))
    if salario == "": # LINHA COM ERRO? #
        salario = float(input("Erro ao preencher! Digite o seu salário[MAIOR QUE 0]: "))

sexo = input("Digite o seu sexo: ")
s = sexo.upper()
while s != 'F' and s != 'M' and s !='Outro':
    s = input("Erro ao preencher! Digite o seu sexo[F, M, Outro]: ")
    if s == "":
        s = input("Erro ao preencher! Digite o seu sexo[F, M, Outro]: ")

print("Obrigado! Seus dados foram registrados!")