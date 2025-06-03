from tkinter import* 
from tkinter import ttk 
from components import placeholder

def abrir_janela_principal(): #função para abrir a tela principal
  
    janela_login.destroy()
    
    
    from main import main  
    main()




def cadastro(): 

    cadastro = Toplevel() 
    cadastro.geometry("400x370") 
    cadastro.title("Tela de cadastro")
    barra2 = Frame(cadastro, width = 410, height=40, bg="#CCCCCC")
    barra2.place(x=0, y=0) 
    Label(barra2,anchor=NW,text="Cadastre um administrador para o sistema.", font=('Helvetica', 12, 'bold'),bg="#CCCCCC").place(x=29, y=9) 
    Label(cadastro,text="Nome do administrador",fg="black",font=('Helvetica', 12,'bold')).place(x=50, y=46)
    Label(cadastro,text="Senha",fg="black",font=('Helvetica', 12,'bold')).place(x=49, y=115)
    Label(cadastro,text="Confirmar senha",fg="black",font=('Helvetica', 12,'bold')).place(x=49, y=195)
    
    entry_nome = Entry(cadastro, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=50, y=70)
    placeholder(entry_nome, "Digite aqui seu nome", cor_placeholder="#A9A9A9")

    entry_senha = Entry(cadastro, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_senha.place(x=50, y=140)
    placeholder(entry_senha, "Digite aqui sua senha", cor_placeholder="#A9A9A9")

    entry_confirm = Entry(cadastro, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_confirm.place(x=50, y=220) 
    placeholder(entry_confirm,"Repita a sua senha", cor_placeholder="#A9A9A9")
    Button(cadastro,text="Voltar",command=cadastro.destroy,font=('Helvetica', 11),width=8, fg="black").place(x=60, y=290) 

    Button(cadastro, text="Finalizar Cadastro",font=('Helvetica', 11),width=15, fg="green").place(x=160, y=290)


    Label(cadastro, text="Senhas diferentes ou usuário já existente",font=('Helvetica', 11), fg="red").place(x=50, y=260) 


    cadastro.mainloop()





janela_login = Tk() 

janela_login.title("Tela de login")
janela_login.geometry("400x250") 




barra = Frame(janela_login, width = 410, height=40, bg="#CCCCCC")
barra.place(x=0, y=0) 
Label(barra,anchor=NW,text="Entre como administrador para acessar o sistema.", font=('Helvetica', 12, 'bold'),bg="#CCCCCC").place(x=5, y=9) 
Label(janela_login,text="Nome do administrador",fg="black",font=('Helvetica', 12,'bold')).place(x=50, y=46)
Label(janela_login,text="Senha",fg="black",font=('Helvetica', 12,'bold')).place(x=49, y=115)
entry_nome = Entry(janela_login, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_nome.place(x=50, y=70)
placeholder(entry_nome, "Digite aqui seu nome", cor_placeholder="#A9A9A9")

entry_senha = Entry(janela_login, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_senha.place(x=50, y=140)
placeholder(entry_senha, "Digite aqui sua senha", cor_placeholder="#A9A9A9")


Button(janela_login,text="Cadastrar",command=cadastro,font=('Helvetica', 11),width=8, fg="black").place(x=100, y=190) 

Button(janela_login, text="Entrar",command=abrir_janela_principal,font=('Helvetica', 11),width=7, fg="green").place(x=200, y=190)


Label(janela_login, text="Usuário ou senha incorreta",font=('Helvetica', 11), fg="red").place(x=99, y=165)
janela_login.mainloop()      


