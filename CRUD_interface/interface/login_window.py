from tkinter import* 
from tkinter import messagebox
from tkinter import ttk 
from components import placeholder
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao,vermelho
import backend

def abrir_janela_principal(): #função para abrir a tela principal
    janela_login.destroy()

    from main import main  
    main()



def cadastro(): 

    cadastro = Toplevel() 
    cadastro.geometry("400x320") 
    cadastro.title("Tela de cadastro") 
    cadastro.configure(bg=verde)
    barra2 = Frame(cadastro, width = 410, height=40, bg=azul)
    barra2.place(x=0, y=0) 
    Label(barra2,anchor=NW,text="Cadastre um administrador para o sistema.", font=('Helvetica', 12, 'bold'),fg="white",bg=azul).place(x=35, y=8) 
    Label(cadastro,text="Nome do administrador",fg="black",font=('Helvetica', 12,'bold'),bg=verde).place(x=65, y=60)
    Label(cadastro,text="Senha",fg="black",font=('Helvetica', 12,'bold'),bg=verde).place(x=65, y=115)
    Label(cadastro,text="Confirmar senha",fg="black",font=('Helvetica', 12,'bold'),bg=verde).place(x=65, y=170)
    
    entry_nome = Entry(cadastro, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=65, y=85)
    placeholder(entry_nome, "Digite aqui seu nome", cor_placeholder="#A9A9A9")

    entry_senha = Entry(cadastro, show="*", width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_senha.place(x=65, y=140)

    entry_confirm = Entry(cadastro, show="*", width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_confirm.place(x=65, y=195) 

    Button(cadastro,text="Voltar",command=cadastro.destroy,font=('Helvetica', 11,'bold'),width=8, fg="black",bg=cor_botao).place(x=80, y=240) 

    def finalizar_cadastro():
        nome_adm = entry_nome.get()
        nome_adm = "" if nome_adm == "Digite aqui seu nome" else nome_adm.title()
        senha = entry_senha.get()
        senha_confirma = entry_confirm.get()

        if nome_adm == "" or senha == "" or senha_confirma == "":
            messagebox.showerror("Cadastro de Administradores", f"Preencha todos os campos.")
            return

        if senha != senha_confirma:
            messagebox.showerror("Cadastro de Administradores", f"As duas senhas são diferentes! Certifique-se de digitar corretamente nos dois campos.")
            return

        if backend.existe_adm(nome_adm):
            messagebox.showerror("Cadastro de Administradores", f"Este nome já tem registro! Utilize outro nome.")
            return
        
        backend.criar_adm(nome_adm, senha)
        messagebox.showinfo("Cadastro de Administradores", f"Cadastro de {nome_adm} realizado com sucesso!")
        abrir_janela_principal()

    Button(cadastro, text="Finalizar Cadastro",command=finalizar_cadastro,font=('Helvetica', 11,'bold'),width=15, fg="green",bg=cor_botao).place(x=180, y=240)

    cadastro.wait_visibility()
    cadastro.grab_set()
    cadastro.mainloop()



janela_login = Tk() 
janela_login.configure(bg=verde)
janela_login.title("Tela de login")
janela_login.geometry("400x250") 


barra = Frame(janela_login, width = 410, height=40, bg=azul)
barra.place(x=0, y=0) 
Label(barra,anchor=NW,text="Entre como administrador para acessar o sistema.", font=('Helvetica', 12, 'bold'),fg="white",bg=azul).place(x=5, y=9) 
Label(janela_login,text="Nome do administrador",fg="black",bg=verde,font=('Helvetica', 12,'bold')).place(x=65, y=60)
Label(janela_login,text="Senha",fg="black",bg=verde,font=('Helvetica', 12,'bold')).place(x=65, y=115)
entry_nome = Entry(janela_login, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_nome.place(x=65, y=85)
placeholder(entry_nome, "Digite aqui seu nome", cor_placeholder="#A9A9A9")

entry_senha = Entry(janela_login, show="*", width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_senha.place(x=65, y=140)


Button(janela_login,text="Cadastrar",command=cadastro,font=('Helvetica', 11,'bold'),width=8, fg="black",bg=cor_botao).place(x=115, y=185) 

def login() -> None:
    nome_adm = entry_nome.get()
    nome_adm = "" if nome_adm == "Digite aqui seu nome" else nome_adm.title()
    senha = entry_senha.get()

    if nome_adm == "Digite aqui seu nome" or nome_adm == "" or senha == "":
        messagebox.showerror("Login de Administradores", f"Preencha todos os campos.")
        return
    
    if not backend.logar_adm(nome_adm, senha):
        messagebox.showerror("Login de Administradores", f"Usuário e/ou senha incorretos!")
        return
    
    messagebox.showinfo("Login de Administradores", f"Login de {nome_adm} realizado com sucesso!")
    abrir_janela_principal()

Button(janela_login, text="Entrar",command=login,font=('Helvetica', 11,'bold'),width=7, fg="green",bg=cor_botao).place(x=215, y=185)

janela_login.mainloop()      


