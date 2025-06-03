from tkinter import* 
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias,check_week  

def novoprofessor(): 
    
    janela_cad = Toplevel() 
    janela_cad.geometry("370x490")
    janela_cad.title("Cadastro de novo professor")
    janela_cad.resizable(width=FALSE, height=FALSE) 
    janela_cad.grab_set()

    label_disc= Label(janela_cad, text="Selecione a matéria do professor substituto", font=('Helvetica', 11, "bold"))
    label_disc.place(x=40, y=140)
    
    Label_nome = Label(janela_cad, text="Nome",font=('Helvetica', 13,"bold"))
    Label_nome.place(x=40, y=20)
    
    entry_nome = Entry(janela_cad, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=50, y=50)
    placeholder(entry_nome, "Nome completo do(a) Professor(a)", cor_placeholder="#A9A9A9") 

    radiobutton_genre(container=janela_cad, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90)
  
    botao_voltar = Button(janela_cad, text="Voltar",font=('Helvetica',10),width=10,command=janela_cad.destroy)
    botao_voltar.place(x=80, y=410) 
    botao_cadastrar= Button(janela_cad, text="Cadastrar", fg="green", font=('Helvetica',10),width=10)
    botao_cadastrar.place(x=205, y=410) 
    

    label_gender = Label(janela_cad, text="Sexo: ", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13, "bold"))
    label_gender.place(x=50, y=90) 
    
    select_opt, mv = combobox_materias(container=janela_cad, x=50, y=190)
    check_vars, _ = check_week(janela_cad, x=80, y=260)
    
 
    #prevenção de bug
    janela_cad.mv = mv  
    janela_cad.check_vars = check_vars
    
    
    return janela_cad  

    
  
    
    



    
