import  pandas as pd


tabela = pd.read_csv("BD_Guaraville.csv")
print(tabela.info())


'''class Cliente:
    def __init__(self, id, nome, cpfCnpj, rgoe, contato1, contato2, email, endereco, numero, bairro, cidade, cep, uf, complemento, datanasc, profissao, estado_civil, nomeConjuge, cpfConjuge, contatoConjuge):
        self.id = id
        self.nome = nome
        self.cpfCnpj = cpfCnpj
        self.rgoe = rgoe
        self.contato1 = contato1
        self.contato2 = contato2
        self.email = email
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.uf = uf
        self.complemento = complemento
        self.datanasc = datanasc
        self.profissao = profissao
        self.estado_civil = estado_civil
        self.nomeConjuge = nomeConjuge
        self.cpfConjuge = cpfConjuge
        self.contatoConjuge = contatoConjuge
        
cliente1 = Cliente ("000001","Reginaldo de Araújo Oliveira", "720.542.633-20", "2697255-93 SSP-CE","(88)99912-0595","0","rao.corretor@gmail.com", "Rua Vereador Pedro Coló", "20","Centro","Guaraciaba do Norte", "62.380-000","CE", "Atrás do Restaurante Opção","19/04/1977","Programador", "Casado", "Josie Sales Matos Oliveira", "055.212.687-07","(88)99926-1738")       

print(f'ID: {cliente1.id}\nNome: {cliente1.nome}\nCPF-CNPJ: {cliente1.cpfCnpj}\nRg-OE: {cliente1.rgoe}\nContato Principal: {cliente1.contato1}\nE-mail: {cliente1.email}') '''      