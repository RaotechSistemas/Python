# Anotações do Curso Python Tkinter - Canal João Ribeiro - YOUTUBE

# Para conferir se há Python na máquina: No terminal, clicar python --version
# Intalar no VSCode a extensão Python da Microsoft (Opcionalmente a extensão Pylint)
# Site para baixar icones favicon gratis:https://iconarchive.com (.ico)
from tkinter import * 
# para baixar toda a biblioteca

menu_inicial = Tk()

menu_inicial.title("Meu 1º App Tkinter") 
#Define o título da Janela
menu_inicial.iconbitmap("favicon.ico")
# para alterar o Favicon da janela ( lembrar de, depois de baixar e colar o arquivo.ico na mesma pasta do projeto, ir nas opções da pasta, Exibir, Opções, alterar as opçoes de pasta e pesquisa, Modo de exibição, de smacar a opção Ocultar as extensões dos tipos de arquivo conhecidos)
menu_inicial.geometry("500x600+800+50")
# Definições iniciais de largura x altura + descolamento horizontal + descolamento vertical

#menu_inicial.resizable(False,False)
# Impede que a janela tenha seus valores geometry alterados (o botão de maximizar também fica inativo) - Os valores 0 e 1 substituem False e True

#menu_inicial.resizable(True,True)
## Permite  que a janela tenha seus valores geometry alterados (o botão de maximizar volta a ficar ativo) - DEFAULT

#menu_inicial.minsize(500,250) 
## Valores mínimos de largura e altura

#menu_inicial.maxsize(800,500) 
## Valores máximos de largura e altura

#menu_inicial.state("zoomed")
## Inicia a janela maximizada

#menu_inicial.state("iconic")
## Inicia a janela minimizada na barra de tarefas

# -------------- WIDGETS -------------- #
#menu_inicial ['bg'] ="grey"
# Define a cor de fundo (bg = background)da janela 


# FRAME 

frame = Frame(menu_inicial)
frame.pack()



#LABEL

label_1 = Label(menu_inicial,
                 text = "label 1",
                 bg='#323232')
label_1.pack() # Configurações básicas de um Label
button1 = Button(label_1,
                 text = "<< VOLTAR",
                 bg='red',
                 font= "bold")
button1.pack(padx = 3, pady = 3)
label_2 = Label(menu_inicial, text = "label 2")
label_2.pack()
button2 = Button(label_2, text = "AVANÇAR >>")
button2.pack(padx = 3, pady = 3)
button3 = Button(menu_inicial, text = "ENTRAR", command = set,
                fg = "red", font = "Verdana 14 underline",
                bd = 2, bg = "light blue", relief = "groove")
                # Configurações básicas de um botão
button3.pack(pady = 5)
# BUTTONS

'''
button1 = Button(label_1, text = "<< VOLTAR")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "AVANÇAR >>")
button2.pack(padx = 3, pady = 3)
button3 = Button(frame, text = "ENTRAR", command = set,
                fg = "red", font = "Verdana 14 underline",
                bd = 2, bg = "light blue", relief = "groove")
button3.pack(pady = 5)
'''
# ENTRY

'''
my_entry = Entry(frame, width = 20)
my_entry.insert(0,'usuário')
my_entry.pack(padx = 5, pady = 5)
my_entry2 = Entry(frame, width = 20)
my_entry2.insert(0,'Senha')
my_entry2.pack(padx = 5, pady = 5)
'''

# CHECK BUTTONS

'''
Var1 = IntVar()
Var2 = IntVar()
 
ChkBttn = Checkbutton(frame, width = 15, variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)
 
ChkBttn2 = Checkbutton(frame, width = 15, variable = Var2)
ChkBttn2.pack(padx = 5, pady = 5)
'''

# RADIO BUTTONS

'''
Var3 = StringVar()
 
RBttn = Radiobutton(frame, text = "Sim", variable = Var3,
                    value = 1)
RBttn.pack(padx = 5, pady = 5)
 
RBttn2 = Radiobutton(frame, text = "Não", variable = Var3,
                     value = 2)
RBttn2.pack(padx = 5, pady = 5)
'''

# MAIN MENU
'''
def save():
    #Code to be written
    pass
 
def load():
    #Code to be written
    pass  

mainmenu = Menu(frame)
mainmenu.add_command(label = "Salvar", command= save)  
mainmenu.add_command(label = "Pesquisar", command= load)
mainmenu.add_command(label = "Sair", command= menu_inicial.destroy)
 
menu_inicial.config(menu = mainmenu)
'''

# COMBOBOX

'''
from tkinter import ttk

vlist = ["BRASIL", "EUA", "JAPÃO",
          "CANADÁ", "ITALIA"]
 
Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Escolha um País")
Combo.pack(padx = 5, pady = 5)
'''

# LISTBOX
'''
listbox = Listbox(menu_inicial)  
listbox.insert(1,"MILHO")  
listbox.insert(2, "LEITE")  
listbox.insert(3, "CAFÉ")  
listbox.insert(4, "CARNES")
listbox.insert(5, "VEGETAIS")  
listbox.pack()  '''

#MENU BUTTONS

'''
MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()
 
Menu1 = Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", variable = Var4)
Menu1.add_checkbutton(label = "Cheese Burger", variable = Var5)
Menu1.add_checkbutton(label = "Salad", variable = Var6)
 
MenuBttn["menu"] = Menu1
 
MenuBttn.pack()

'''

# CANVAS

'''frame.pack(expand = True, fill=BOTH)
 
canvas = Canvas(frame,bg='white', width = 300,height = 300)
 
coordinates = 20, 50, 210, 230
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
 
canvas.pack(expand = True, fill = BOTH)'''

# SCALES

'''
Scala = Scale(frame, from_=10, to=0)
Scala.pack(padx=5, pady=5)
 
Scala2 = Scale(frame, from_=0, to=15, orient=HORIZONTAL)
Scala2.pack(padx=5, pady=5)
'''

# SCROOLBAR
'''
mylabel = Label(menu_inicial, text ='Scrollbars', font = "30")  
mylabel.pack() 
 
myscroll = Scrollbar(menu_inicial) 
myscroll.pack(side = RIGHT, fill = Y) 
 
mylist = Listbox(menu_inicial, yscrollcommand = myscroll.set )  
for line in range(1, 100): 
    mylist.insert(END, "Number " + str(line)) 
mylist.pack(side = LEFT, fill = BOTH )    
 
myscroll.config(command = mylist.yview)
'''

# TOPLEVEL

'''
def NewWindow():
    window = Toplevel()
    window.geometry('150x150')
    newlabel = Label(window, text = "Settings Window")
    newlabel.pack()

myframe = Frame(menu_inicial)
myframe.pack()
 
mybutton = Button(myframe, text = "Settings", command = NewWindow)
mybutton.pack(pady = 10)

'''
# ------------- CENTRALIZAR FORMULÁRIO ------------- #
'''
# Dimensões da janela
largura = 600
altura = 400
# Resolução da Tela da máquina
largura_screen = menu_inicial.winfo_screenmmwidth()
altura_screen = menu_inicial.winfo_screenmmheight()
# Posicionamento da janela
pos_x = largura_screen/2 - altura/2
pos_y = altura_screen/2 - altura/2
# Definir a Geometry
menu_inicial.geometry ("%dx%d+%d+%d" % (largura,altura,pos_x,pos_y))
'''


#-----------------------------------------#
menu_inicial.mainloop() 
# Loop que mantém a janela aberta até ser fechada pelo usuário ou por alguma programação. Deve ser colocado ao final do código
