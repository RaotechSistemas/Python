import PySimpleGUI as sg

class TelaPython:
    #Layout
    layout =[
        [sg.Text('Nome', size=(5,0)),sg.Input(size=(30,0), key = 'nome')],
        [sg.Text('idade', size =(5,0)),sg.Input(size=(5,0), key = 'idade')],
        [sg.Text('Quais emails você aceita?')],
        [sg.Checkbox('Gmail', key = 'gmail'),sg.Checkbox('OutLook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')],
        [sg.Button('Salvar')]
    ]
    #Janela
    janela =sg.Window('Dados do Usuário').layout(layout)

    #extrair dados
    self.button, self.values = janela.Read()

def Iniciar(self):
     nome=self.values['nome']
     idade=self.values['idade']
     
     print(self.values) 

tela = TelaPython()
tela.Iniciar()
    

