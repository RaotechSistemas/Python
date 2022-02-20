from tkinter import *
class Janela:
    
    def __init__(self, toplevel):
        self.fr1 = Frame (toplevel)
        self.fr1.pack()
        self.botao1 = Button (self.fr1, text ="Olá", bg = 'blue')
        self.botao1 ['font'] = ('Verdana', '12','italic', 'bold')
        self.botao1 ['height'] = 2
        self.botao1 ['width'] =12
        self.botao1.pack()
        
        self.botao2 = Button (self.fr1, bg = 'red', font = ('Times', "16"), fg = 'white')
        self.botao2 ['text'] = "Mundo!"
        self.botao2 ['height'] = 2
        self.botao2 ['width'] = 12
        self.botao2.pack()
        
raiz = Tk()
Janela (raiz)
raiz.mainloop()    