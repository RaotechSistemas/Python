
with open('D:\Python\Exercicios\BD_clientes.csv','r',encoding="utf-8")  as arquivo:
    linhas = arquivo.read()
    linhas = linhas.split('\n')
    #header = next (leitor)
    for linha in linhas:
        linha = linha.split(",")
        #if linha[0] == "C.01/02":
        print (linha)
