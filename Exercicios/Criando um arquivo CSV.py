import csv
with open('D:\Python\Exercicios\BD_clientes.csv', 'w',encoding ='utf-8', newline='') as clientes:
    escritor = csv.writer(clientes)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['João', 'Da Silva', 'js@gmail.com', 'masculino'])
    escritor.writerow(['Maria', 'Das Graças', 'ms@yahoo.com', 'feminino'])