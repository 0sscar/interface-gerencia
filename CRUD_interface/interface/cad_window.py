from tkinter import* 
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias,check_week  
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao


def novoprofessor(): 
    
    janela_cad = Toplevel() 
    janela_cad.geometry("370x490")
    janela_cad.title("Cadastro de novo professor")
    frame_tabela = Frame(janela_cad,width=210, height=130,bg=cor_tabela) 
    frame_tabela.place(x=80, y=260)
    janela_cad.configure(bg=branco)
    janela_cad.resizable(width=FALSE, height=FALSE) 
    janela_cad.grab_set()

    label_disc= Label(janela_cad, text="Selecione a matéria do professor substituto", font=('Helvetica', 11, "bold"),bg=branco)
    label_disc.place(x=40, y=156)
    
    Label_nome = Label(janela_cad, text="Nome",font=('Helvetica', 13,"bold"),bg=branco)
    Label_nome.place(x=40, y=20)
    
    entry_nome = Entry(janela_cad, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=50, y=50)
    placeholder(entry_nome, "Nome completo do(a) Professor(a)", cor_placeholder="#A9A9A9") 

    radiobutton_genre(container=janela_cad, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90)
  
    botao_voltar = Button(janela_cad, text="Voltar",font=('Helvetica',10,'bold'),bg=cor_botao,width=10,command=janela_cad.destroy)
    botao_voltar.place(x=80, y=410) 
    botao_cadastrar= Button(janela_cad, text="Cadastrar", fg="green",bg=cor_botao, font=('Helvetica',10,'bold'),width=10)
    botao_cadastrar.place(x=205, y=410) 
    

    label_gender = Label(janela_cad, text="Sexo: ", anchor=NW, fg="#0C0C0C", font=('Helvetica', 13, "bold"),bg=branco)
    label_gender.place(x=50, y=90) 
    
    select_opt, mv = combobox_materias(container=janela_cad, x=50, y=190)
    check_vars, _ = check_week(frame_tabela)
    
 
    #prevenção de bug
    janela_cad.mv = mv  
    janela_cad.check_vars = check_vars
    
    
    return janela_cad  

    
  
    
    



    
