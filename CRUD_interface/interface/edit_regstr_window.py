from tkinter import* 
from tkinter import ttk  
from components import placeholder, radiobutton_genre, combobox_materias,check_week  




def editprofessor(dados_professor):
 
    janela_edt = Toplevel() 
    janela_edt.geometry("370x490")
    janela_edt.title("Editar Professor")
    janela_edt.resizable(width=FALSE, height=FALSE) 
    janela_edt.grab_set()
    janela_edt.configure(bg="#FFFFFF")

    # Variáveis para armazenar os controles
    controles = {}

    # Preenche o nome
    Label(janela_edt, text="Nome", font=('Helvetica', 13, "bold"), bg="#FFFFFF").place(x=40, y=20)
    entry_nome = Entry(janela_edt, width=30, font=('Helvetica', 12))
    entry_nome.place(x=50, y=50)
    entry_nome.insert(0, dados_professor[1])  # Preenche com o nome
    controles['entry_nome'] = entry_nome

    # Preenche o sexo
    Label(janela_edt, text="Sexo:", font=('Helvetica', 13, "bold"), bg="#FFFFFF").place(x=50, y=90)
    sexo_var = StringVar(value="masculino" if dados_professor[0] == "M" else "Feminino")
    radiobutton_genre(container=janela_edt, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90, var=sexo_var)
    controles['sexo_var'] = sexo_var

    # Preenche a matéria
    Label(janela_edt, text="Selecione a matéria", font=('Helvetica', 11, "bold"), bg="#FFFFFF").place(x=40, y=140)
    select_opt, materia_var = combobox_materias(container=janela_edt, x=50, y=190)
    materia_var.set(dados_professor[2])  # Preenche a disciplina
    controles['materia_var'] = materia_var

    # Tabela de disponibilidade
    check_vars, _ = check_week(janela_edt, x=80, y=260)
    controles['check_vars'] = check_vars

    # Botões
    Button(janela_edt, text="Voltar", font=('Helvetica',10), width=10,
          command=janela_edt.destroy).place(x=80, y=410) 
    
    Button(janela_edt, text="Salvar", fg="green", font=('Helvetica',10), width=10,
          command=lambda: salvar_edicao(controles)).place(x=205, y=410)

    return janela_edt

def salvar_edicao(controles):
    """Função para salvar as alterações"""
    # Obter os valores dos controles
    nome = controles['entry_nome'].get()
    sexo = controles['sexo_var'].get()
    materia = controles['materia_var'].get()
    disponibilidade = controles['check_vars']
    
    # Aqui você implementa a lógica para atualizar o registro
    print(f"Dados editados - Nome: {nome}, Sexo: {sexo}, Matéria: {materia}")
    # ... sua lógica de atualização no banco de dados ou na treeview

    
  
    
    


