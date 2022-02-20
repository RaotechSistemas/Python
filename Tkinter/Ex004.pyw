from tkinter import *
class Packing:
    
    def __init__(self, instancia_Tk):
        
        self.container1 = Frame (instancia_Tk)
        self.container2 = Frame (instancia_Tk)   
        self.container3 = Frame (instancia_Tk) 
        
        self.container1.pack()
        self.container2.pack()   
        self.container3.pack() 
            # Container 1 com apenas 1 botão
        Button (self.container1, text = 'Cancelar', bg='red', font=( 'bold', 12, 'italic'),fg='white').pack()
            # Container 2 com 2 botões
        Button (self.container2, text = 'Botão 02', font="Verdana").pack(side=LEFT)
        Button (self.container2, text = 'Botão 03',height = 3, width=15).pack(side=LEFT)
            # Container 3 com 3 botões
        Button (self.container3, text = 'Botão 04', fg = 'yellow', bg='black').pack(side=LEFT)
        Button (self.container3, text = 'Botão 05', font =("Times", '16')).pack(side=LEFT)
        Button (self.container3, text = 'Botão 06', width=12).pack(side=LEFT)
        
       
        
raiz = Tk()
Packing (raiz)
raiz.mainloop()    