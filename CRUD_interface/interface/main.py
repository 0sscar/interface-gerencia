from tkinter import* 
from tkinter import messagebox
from tkinter import ttk 
from random import choice
from cad_window import novoprofessor
from registr_window import exibir_registro  
from components import placeholder, radiobutton_genre, combobox_materias,check_week, checkbutton_genre
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao, vermelho
import backend
from disponibilidade import calcular_disponibilidade
from atualizar_treeview import atualizar_treeview, atualizar_treeview_filtrada



janela = Tk()  
janela.geometry("1043x593")
janela.title("Sistema de Professores Substitutos")
janela.configure(bg=verde)
janela.resizable(width=FALSE, height=FALSE)#janela fixa
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)


style = ttk.Style()
style.theme_use("default")  

#xonfiguração do estilo da Treeview
style.configure("Custom.Treeview",
    background="#EDEAE3",
    foreground="#333333",
    rowheight=25,
    fieldbackground="#FFFFFF",
    bordercolor="#E1E1E1",
    borderwidth=1,
    font=('Helvetica', 10),
    alternatingrowbackground="#F9F9F9"  #
)

#estilo do cabeçalho
style.configure("Custom.Treeview.Heading",
    background="#CCCCCC",  
    foreground="#333333",  
    padding=9,  
    font=('Arial', 10, 'bold')  
)

#estilo quando uma linha está selecionada
style.map("Custom.Treeview",
    background=[('selected', '#E6F2FF')],  
    foreground=[('selected', '#000000')]  
)

#estilo do Combobox
style.configure('TCombobox',
    foreground='black',
    background='white',
    fieldbackground='white',
    selectbackground='white',
    selectforeground='black',
    padding=5,
    relief='flat',
    font=('Helvetica', 14)
)

style.map('TCombobox',
    fieldbackground=[('readonly', 'white')],
    selectbackground=[('readonly', "#FFFFFF")],  # Azul claro ao selecionar
    selectforeground=[('readonly', 'black')],
    background=[('readonly', 'white')]
)



#divisão de elementos 
frame1 = Frame(janela, width = 410, height=600, bg=branco)
frame1.grid(row=0, column=0) 

frame2 = Frame(janela,width=640, height=600, relief="flat")
frame2.grid(row=0, column=1)

frame3 = Frame(janela,width= 700, height=89, bg=verde)
frame3.place(x=410,y=0)


frame4 = Frame(janela,width= 700, height=89, bg=verde)
frame4.place(x=410,y=504) 

frame5 = Frame(janela,width=210, height=130,bg=cor_tabela) 
frame5.place(x=95,y=240)




label_registro = Label(frame3, text="Registros", anchor=CENTER, fg="white", bg=azul,width=38,font=('Arial',"20","bold")) 
label_registro.place(x=0,y=0)

label_nome = Label( frame1, text="Insira o nome do professor que deseja buscar", anchor=NW,fg="#0C0C0C", bg=branco, font=('Helvetica', 12,"bold")) 
label_nome.place(x=25, y=22) 

entry_nome = Entry(frame1, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_nome.place(x=65, y=50)
placeholder(entry_nome, "Nome do(a) Professor(a)", cor_placeholder="#A9A9A9") 

filtro_check_vars, _ = check_week(frame5)

Label_click = Label(frame3, text="Clique em um registro para mais informações e opções", font=('Helvetica', 10,'bold'),bg=verde) 
Label_click.place(x=150, y= 52)

#checkbutton
sexo_var = checkbutton_genre(container=frame1, x_label=65, y_label=90, x_inicial_rb=120, y_rb=90)



#combobox//optionmenu
combobox, mv =combobox_materias(container=frame1,x=65,y=160)


label_menu = Label(frame1, text="Selecione sua matéria", anchor=NW, fg="#0C0C0C", bg=branco, font=('Helvetica', 14,"bold"))
label_menu.place(x=90, y=129)



#####criacao da tabela#########




style.layout("Custom.Treeview.Item", [
    ('Treeitem.padding', {
        'sticky': 'nswe',
        'children': [
            ('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
            ('Treeitem.image', {'side': 'left', 'sticky': ''}),
            ('Treeitem.text', {'side': 'left', 'sticky': ''}),
        ],
        'border': "1"  # Bordas em todos os lados
    })
])



campos = ["ID", "Sexo", "Nome", "Disciplina", "Disponibilidade"]
campos_exibidos = (campos[1], campos[2], campos[3]) 

tabela =  ttk.Treeview(frame2, selectmode="extend",columns=campos, show="headings",height=15,style="Custom.Treeview") 
tabela.place(x=10, y=10, width=620, height=580)
vscroll = ttk.Scrollbar(frame2, orient="vertical", command=tabela.yview) 

#hscroll = ttk.Scrollbar(frame2, orient="horizontal", command=tabela.xview) 
tabela.configure(yscrollcommand=vscroll.set) #xscrollcommand=hscroll.set)



#posicionando elementos  
tabela.grid(column=0,row=0,sticky="nsew") 
vscroll.grid(column=1,row=0,sticky="ns") 
#hscroll.grid(column=0,row=1,sticky="ew") 

frame2.grid_rowconfigure(0, weight=1)  
frame2.grid_columnconfigure(0, weight=1)  

header_anchor = ["nw", "nw", "nw", "nw", "nw"]    
header_size = [0, 54, 200, 170, 0] 

for i in range(len(campos)):
    tabela.heading(i, text=campos[i].title(), anchor=W)
    tabela.column(i, width=header_size[i], anchor=header_anchor[i])

tabela["displaycolumns"] = campos_exibidos


def select_tree(event):
    """Abre a janela de registro com os dados do professor selecionado"""
    item_selecionado = tabela.focus()
    
    if item_selecionado:
        dados_professor = tabela.item(item_selecionado, 'values')
        print("seleção na tabela, dados_professor=", dados_professor)
        exibir_registro(tabela, dados_professor)  # Chama a função passando os dados

#vinculando o evento
tabela.bind("<Double-1>", select_tree)
tabela.configure(selectmode="browse")  

# o relatório é atualizado em tempo real quando acontece algo no backend.
# essa mensagem é só pra direcionar o usuário ao arquivo.
def gerar_relatorio() -> None:
    messagebox.showinfo("Geração de Relatório", "Relatório gerado com sucesso! Confira o arquivo relatorios.txt na pasta do programa.")

botao_relatorio = Button(frame4,width=15, height=1, text="Gerar Relatório", command=gerar_relatorio, anchor=CENTER,fg="black", bg=cor_botao,font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_relatorio.place(x=110, y=40) 

botao_cadastro = Button(frame4,width=29, height=1, text="Cadastrar Novo Professor Substituto",anchor=CENTER,fg="#FFFFFF", bg=verde_claro,font=("Ivy 10 bold"), relief= "raised", overrelief="ridge", command=lambda: novoprofessor(tabela))
botao_cadastro.place(x=290, y=40)

def aplicar_filtro() -> None:
    nome = entry_nome.get().title()
    nome = "" if nome == "Nome do(a) Professor(a)".title() else nome

    sexo = ""
    if sexo_var[0].get() and not sexo_var[1].get(): sexo = "M"
    elif not sexo_var[0].get() and sexo_var[1].get(): sexo = "F"
    #sexo = "M" if sexo_var.get() == "Masculino" else "F"

    disciplina = combobox.get().title()
    disciplina = "" if disciplina == "Disciplina" else disciplina

    disponibilidade = calcular_disponibilidade(filtro_check_vars)

    atualizar_treeview_filtrada(tabela, nome=nome, sexo=sexo, disciplina=disciplina, disponibilidade=disponibilidade)

def resetar_filtro() -> None:
    sexo_var[0].set("False")
    sexo_var[1].set("False")
    combobox.set("")
    for turno in filtro_check_vars:
        for dia in turno:
            dia.set(False)
    atualizar_treeview(tabela)


botao_filtro = Button(frame1,width=13, height=2, text="Aplicar Filtro", command=aplicar_filtro, anchor=CENTER,fg="#FFFFFF", bg="#54A9BE",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_filtro.place(x=230, y=440)

botao_filtro = Button(frame1,width=13, height=2, text="Resetar Filtro", command=resetar_filtro, anchor=CENTER,fg="#FFFFFF", bg=vermelho,font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_filtro.place(x=70, y=440)


atualizar_treeview(tabela)
janela.mainloop()      
