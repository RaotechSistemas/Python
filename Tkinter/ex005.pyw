from tkinter import *
class Janela:
    
    def __init__(self, toplevel):
        
        self.frame = Frame (toplevel)
        self.frame.pack()
        
        self.container1 = Frame (toplevel)
        self.container2 = Frame (toplevel)
        self.container3 = Frame (toplevel)
        self.container4 = Frame (toplevel)
        
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        self.container4.pack()
        
        Label (self.container1).pack
        self.texto = Label (self.frame, text = "Projeto Lotear - Gerenciador de Loteamentos ", width = 100, height = 3, fg='blue', font=('Verdana' , '20', 'italic', 'bold'))
        self.texto.pack()
                
        
        Button (self.container2, text = 'Dados da Empresa', width=20).pack(side=LEFT)
        Button (self.container2, text = 'Loteamentos', width=20).pack(side=LEFT)
        Button (self.container2, text = 'Lotes', width=20).pack(side=LEFT)
        Button (self.container2, text = 'Clientes', width=20).pack(side=LEFT)
        Button (self.container2, text = 'Contratos', width=20).pack(side=LEFT)
        Button (self.container2, text = 'Botão 06', width=20).pack(side=LEFT)
        
         
        self.botaonovo = Button (self.container3, text = 'Novo', width=20)
        self.botaonovo.bind("<Button-1>",self.muda_cor)
        
        self.botaoeditar = Button (self.container3, text = 'Editar', width=20)
        self.botaoeditar.bind("<Button-1>",self.muda_cor)
        
        self.botaoconsultar = Button (self.container3, text = 'Consultar', width=20)
        self.botaoconsultar.bind("<Button-1>",self.muda_cor)
        
        self.botaoexcluir = Button (self.container3, text = 'Excluir', width=20)
        self.botaoexcluir.bind("<Button-1>",self.muda_cor)
        
        self.botaonovo.pack(side=RIGHT)
        self.botaoeditar.pack(side=RIGHT)
        self.botaoconsultar.pack(side=RIGHT)
        self.botaoexcluir.pack(side=RIGHT)
        
        Label (self.container4).pack
        self.texto2 = Label (self.frame, text = " Container 04", width = 100, height = 3, fg='blue', font=('Verdana' , '20', 'italic', 'bold'))
        self.texto2.pack()
        
    def muda_cor (self, event):
        # Muda a cor do botão!
               
        Label (self.container4).pack
        self.texto2 = Label (self.frame, text = "OK ", width = 100, height = 3, fg='blue', font=('Verdana' , '20', 'italic', 'bold'))
        self.texto2.pack()
               
                        
       
        
raiz = Tk()
Janela (raiz)
raiz.mainloop()    