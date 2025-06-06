from tkinter import* 
from tkinter import messagebox
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias,check_week  
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao
import backend
from disponibilidade import calcular_disponibilidade
from atualizar_treeview import atualizar_treeview
import re


def novoprofessor(treeview): 
    
    janela_cad = Toplevel() 
    janela_cad.geometry("370x490")
    janela_cad.title("Cadastro de Novo Professor")
    frame_tabela = Frame(janela_cad,width=210, height=130,bg=cor_tabela) 
    frame_tabela.place(x=80, y=260)
    janela_cad.configure(bg=branco)
    janela_cad.resizable(width=FALSE, height=FALSE) 
    janela_cad.grab_set()

    label_disc= Label(janela_cad, text="Selecione a matéria do professor substituto", font=('Helvetica', 11, "bold"),bg=branco)
    label_disc.place(x=30, y=156)
    
    Label_nome = Label(janela_cad, text="Nome",font=('Helvetica', 13,"bold"),bg=branco)
    Label_nome.place(x=45, y=20)
    
    entry_nome = Entry(janela_cad, width=30, justify="left", relief="solid", font=('Helvetica', 12))
    entry_nome.place(x=45, y=45)
    placeholder(entry_nome, "Nome completo do(a) Professor(a)", cor_placeholder="#A9A9A9")

    label_gender = Label(janela_cad, text="Sexo: ", anchor=NW, fg="#0C0C0C", font=('Helvetica', 13, "bold"),bg=branco)
    label_gender.place(x=50, y=90)
    sexo_var = radiobutton_genre(container=janela_cad, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90)
      
    combobox, mv = combobox_materias(container=janela_cad, x=50, y=190)
    check_vars, _ = check_week(frame_tabela)

    #prevenção de bug
    janela_cad.mv = mv  
    janela_cad.check_vars = check_vars

    botao_voltar = Button(janela_cad, text="Voltar",font=('Helvetica',10,'bold'),bg=cor_botao,width=10,command=janela_cad.destroy)
    botao_voltar.place(x=80, y=410)

    def cadastrar_professor() -> None:
        nome_prof = entry_nome.get()
        nome_prof = "" if nome_prof == "Nome completo do(a) Professor(a)" else nome_prof.title().strip()
        nome_prof = re.sub(r"\s+", " ", nome_prof)

        sexo = "M" if sexo_var.get() == "Masculino" else "F"

        disciplina = combobox.get().title()
        disciplina = "" if disciplina == "Disciplina" else disciplina

        disponibilidade = calcular_disponibilidade(check_vars)

        #print(f"nome_prof={nome_prof}, sexo={sexo}, disciplina={disciplina}, disponibilidade={disponibilidade}")

        if nome_prof == "" or disciplina == "":
            messagebox.showerror("Cadastro de Professores", "Preencha todos os campos.")
            return
        
        if disponibilidade == 0:
            prosseguir = messagebox.askyesno("Cadastro de Professores", f"Você não definiu a disponibilidade de {nome_prof}. Deseja cadastrar mesmo assim?")
            if not prosseguir:
                return

        backend.criar_prof(nome_prof, sexo, disciplina, disponibilidade)
        messagebox.showinfo("Cadastro de Professores", f"Cadastro de {nome_prof} realizado com sucesso!")
        janela_cad.destroy()
        atualizar_treeview(treeview)

    botao_cadastrar= Button(janela_cad, text="Cadastrar", command=cadastrar_professor, fg="green",bg=cor_botao, font=('Helvetica',10,'bold'),width=10)
    botao_cadastrar.place(x=205, y=410) 

    return janela_cad  

    
  
    
    



    
