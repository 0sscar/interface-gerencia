from tkinter import* 
from tkinter import ttk 
from random import choice
from cad_window import novoprofessor
from registr_window import exibir_registro  
from components import placeholder, radiobutton_genre, combobox_materias,check_week 


janela = Tk()  
janela.geometry("1043x593")
janela.title("Sistema de Professores Substitutos")
janela.configure(bg="#0C0C0C")
janela.resizable(width=FALSE, height=FALSE)#janela fixa
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# Configuração do estilo ANTES de criar os widgets
style = ttk.Style()
style.theme_use("default")  # Usamos o tema base para personalização

# Configuração do estilo da Treeview
style.configure("Custom.Treeview",
    background="#EDEAE3",
    foreground="#333333",
    rowheight=25,
    fieldbackground="#FFFFFF",
    bordercolor="#E1E1E1",
    borderwidth=1,
    font=('Helvetica', 10),
    # Adiciona cores alternadas
    alternatingrowbackground="#F9F9F9"  # Cinza muito claro para linhas alternadas
)

# Estilo do cabeçalho
style.configure("Custom.Treeview.Heading",
    background="#CCCCCC",  # Cor de fundo do cabeçalho
    foreground="#333333",  # Cor do texto do cabeçalho
    padding=9,  # Espaçamento interno
    font=('Arial', 10, 'bold')  # Fonte em negrito
)

# Estilo quando uma linha está selecionada
style.map("Custom.Treeview",
    background=[('selected', '#E6F2FF')],  # Azul claro quando selecionado
    foreground=[('selected', '#000000')]  
)

# Estilo do Combobox
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
frame1 = Frame(janela, width = 410, height=600, bg="#FFFFFF")
frame1.grid(row=0, column=0) 

frame2 = Frame(janela,width=640, height=600,bg="#C5C5C5", relief="flat")
frame2.grid(row=0, column=1)

frame3 = Frame(janela,width= 700, height=89, bg="#AF0306")
frame3.place(x=410,y=0)


frame4 = Frame(janela,width= 700, height=89, bg="#22E222")
frame4.place(x=410,y=504) 

frame5 = Frame(janela,width=210, height=130,bg="#E7E5DF") 
frame5.place(x=85,y=240)



'''
def placeholder(entry, texto_placeholder, cor_placeholder="gray"):
    # Adiciona o texto inicial
    entry.insert(0, texto_placeholder)
    entry.config(fg=cor_placeholder)

    # Função para limpar o placeholder quando o Entry recebe foco
    def on_entry_click(event):
        if entry.get() == texto_placeholder:
            entry.delete(0, END)
            entry.config(fg="black")  # Cor do texto normal

    # Função para restaurar o placeholder se o Entry estiver vazio
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, texto_placeholder)
            entry.config(fg=cor_placeholder)

    # Vincula os eventos
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)
'''
label_registro = Label(frame3, text="Registros", anchor=CENTER,fg="#0C0C0C",  bg="#FFFFFF",width=38,font=('Arial',"20","bold")) 
label_registro.place(x=0,y=0)

label_nome = Label( frame1, text="Insira o nome do professor", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13,"bold")) 
label_nome.place(x=50, y=20) 

entry_nome = Entry(frame1, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_nome.place(x=50, y=50)
placeholder(entry_nome, "Nome do(a) Professor(a)", cor_placeholder="#A9A9A9") 

Label_click = Label(frame3, text="Clique em um registro para mais informações e opções", font=('Helvetica', 10)) 
Label_click.place(x=150, y= 52)



#input de email
'''
label_email = Label( frame1, text="Insira o email", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14)) 
label_email.place(x=50, y=90)

entry_email = Entry(frame1, width=45, justify="left", relief="solid",text="Nome do professor") 
entry_email.place(x=50, y=120)
placeholder(entry_email, 'Insira o email',cor_placeholder="#A9A9A9")
'''


# RadioButtons
radiobutton_genre(container=frame1, x_label=50, y_label=90, x_inicial_rb=120, y_rb=90)


label_gender = Label(frame1, text="Sexo: ", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13, "bold"))
label_gender.place(x=50, y=90)






# Combobox//optionmenu
select_opt, mv =combobox_materias(container=frame1,x=50,y=160)


label_menu = Label(frame1, text="Selecione sua matéria", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14))
label_menu.place(x=50, y=127)




#botoes
#editar depois 
botao_inserir = Button(frame4,width=15, height=1, text="Gerar Relatório",anchor=CENTER,fg="#FFFFFF", bg="#00BF62",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_inserir.place(x=110, y=40) 


botao_cadastro = Button(frame4,width=29, height=1, text="Cadastrar Novo Professor Substituto",anchor=CENTER,fg="#FFFFFF", bg="#FF3131",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge", command=novoprofessor )
botao_cadastro.place(x=290, y=40) 


botao_atualizar = Button(frame1,width=13, height=2, text="Aplicar Filtro",anchor=CENTER,fg="#FFFFFF", bg="#5372FF",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_atualizar.place(x=130, y=440)



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



campos = ["Sexo","Nome", "Disciplina"] 

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

header = ["nw","nw", "nw","nw"]    
header_size=[54,200,170] 
n=0
##############################################





#dados para testar a tabela
for i in campos:
    tabela.heading(i, text=i.title(), anchor=W) 
    tabela.column(i,width=header_size[n],anchor=header[n])

    n+=1 


from random import choice

sexos = ["M", "F"]
nomes = ["Carlos", "Ana", "Pedro", "Mariana"] 
disciplinas = ["Matemática", "Português", "História"] 

for _ in range(50):  # 50 registros de teste
    tabela.insert("", "end", values=(
        choice(sexos),
        choice(nomes),
        choice(disciplinas)
    ))



def select_tree(event):
    """Abre a janela de registro com os dados do professor selecionado"""
    item_selecionado = tabela.focus()
    
    if item_selecionado:
        dados_professor = tabela.item(item_selecionado, 'values')
        exibir_registro(dados_professor)  # Chama a função passando os dados

# Vinculando o evento
tabela.bind("<Double-1>", select_tree)
tabela.configure(selectmode="browse")  # Para seleção de uma linha por vez
# Substitua o código atual da tabela por:
check_week(frame5)


    
    




janela.mainloop()      
