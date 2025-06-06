from tkinter import* 
from tkinter import messagebox
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias,check_week  
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao,vermelho
from disponibilidade import calcular_disponibilidade, definir_check_vars
import backend
from atualizar_treeview import atualizar_treeview
import re



def editprofessor(treeview, variaveis, dados_professor):
    janela_edt = Toplevel() 
    janela_edt.geometry("370x490")
    janela_edt.title("Editar Professor")
    janela_edt.resizable(width=FALSE, height=FALSE) 
    janela_edt.grab_set()
    janela_edt.configure(bg=branco)

    # Variáveis para armazenar os controles
    controles = {}
    controles["id"] = int(dados_professor[0])
     
    frame_tabela = Frame(janela_edt,width=210, height=130,bg=cor_tabela) 
    frame_tabela.place(x=80, y=260)
    # Preenche o nome
    Label(janela_edt, text="Nome", font=('Helvetica', 13, "bold"), bg=branco).place(x=40, y=20)
    entry_nome = Entry(janela_edt, width=30, font=('Helvetica', 12))
    entry_nome.place(x=50, y=50)
    entry_nome.insert(0, dados_professor[2])  # Preenche com o nome
    controles['entry_nome'] = entry_nome

    # Preenche o sexo
    Label(janela_edt, text="Sexo:", font=('Helvetica', 13, "bold"), bg=branco).place(x=50, y=90)
    sexo_var = StringVar(value="Masculino" if dados_professor[1] == "M" else "Feminino")
    radiobutton_genre(container=janela_edt, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90, var=sexo_var)
    controles['sexo_var'] = sexo_var

    # Preenche a matéria
    Label(janela_edt, text="Selecione a matéria", font=('Helvetica', 11, "bold"), bg=branco).place(x=40, y=140)
    select_opt, materia_var = combobox_materias(container=janela_edt, x=50, y=190)
    materia_var.set(dados_professor[3])  # Preenche a disciplina
    controles['materia_var'] = materia_var

    # Tabela de disponibilidade
    check_vars, _ = check_week(frame_tabela, disponibilidade=int(dados_professor[4]))
    controles['check_vars'] = check_vars

    # Botões
    Button(janela_edt, text="Voltar", font=('Helvetica',10,'bold'), width=10,bg=cor_botao,command=janela_edt.destroy).place(x=80, y=410) 

    def salvar_edicao(controles) -> None:
        """Função para salvar as alterações"""
        # Obter os valores dos controles
        id = controles["id"]
        nome = re.sub(r"\s+", " ", controles['entry_nome'].get().title().strip())
        sexo = "M" if controles['sexo_var'].get() == "Masculino" else "F"
        disciplina = controles['materia_var'].get().title()
        disponibilidade = calcular_disponibilidade(controles['check_vars'])
        
        print(f"Dados editados - Nome: {nome}, Sexo: {sexo}, Disciplina: {disciplina}, Disponibilidade: {disponibilidade}")

        variaveis["id"].set(id)
        variaveis["nome"].set(nome)
        variaveis["sexo"].set(sexo)
        variaveis["disciplina"].set(disciplina)
        variaveis["disponibilidade"].set(disponibilidade)
        definir_check_vars(variaveis["check_vars"], disponibilidade)
        backend.atualizar_prof(id, nome, sexo, disciplina, disponibilidade)
        messagebox.showinfo("Editar Cadastro", f"Cadastro de {nome} foi editado com sucesso!")
        janela_edt.destroy()
        atualizar_treeview(treeview)

    Button(janela_edt, text="Salvar", fg="green", font=('Helvetica',10,'bold'), width=10,bg=cor_botao,command=lambda: salvar_edicao(controles)).place(x=205, y=410)

    return janela_edt

  
    
    


