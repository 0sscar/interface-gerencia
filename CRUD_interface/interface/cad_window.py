from tkinter import* 
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias 

def novoprofessor(): 
    
    janela_cad = Toplevel() 
    janela_cad.geometry("370x490")
    janela_cad.title("Cadastro de novo professor")
    
    Label_nome = Label(janela_cad, text="Nome",font=('Helvetica', 13,"bold"))
    Label_nome.place(x=40, y=20)
    
    entry_nome = Entry(janela_cad, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=50, y=50)
    placeholder(entry_nome, "Nome completo do(a) Professor(a)", cor_placeholder="#A9A9A9") 

    radiobutton_genre(container=janela_cad, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90)


    label_gender = Label(janela_cad, text="Sexo: ", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13, "bold"))
    label_gender.place(x=50, y=90) 
    
    
    combobox_materias(container=janela_cad,x=50,y=190)
    

    
