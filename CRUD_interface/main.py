from tkinter import* 
from tkinter import ttk 
from random import choice

janela = Tk()  
janela.geometry("1043x593")
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
    foreground=[('selected', '#000000')]  # Texto preto quando selecionado
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

frame5 = Frame(janela,width=300, height=190,bg="#FF7900") 
frame5.place(x=80,y=240)

def criar_placeholder(entry, texto_placeholder, cor_placeholder="gray"):
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

label_registro = Label(frame3, text="Registros", anchor=CENTER,fg="#0C0C0C",  bg="#FFFFFF",width=38,font=('Arial',"20","bold")) 
label_registro.place(x=0,y=0)

label_nome = Label( frame1, text="Insira o nome do professor", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13,"bold")) 
label_nome.place(x=50, y=20) 

entry_nome = Entry(frame1, width=30, justify="left", relief="solid", font=('Helvetica', 12))
entry_nome.place(x=50, y=50)
criar_placeholder(entry_nome, "Nome do(a) Professor(a)", cor_placeholder="#A9A9A9") 

Label_click = Label(frame3, text="Clique em um registro para mais informações e opções", font=('Helvetica', 10)) 
Label_click.place(x=150, y= 52)



#input de email
'''
label_email = Label( frame1, text="Insira o email", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14)) 
label_email.place(x=50, y=90)

entry_email = Entry(frame1, width=45, justify="left", relief="solid",text="Nome do professor") 
entry_email.place(x=50, y=120)
criar_placeholder(entry_email, 'Insira o email',cor_placeholder="#A9A9A9")
'''


# RadioButtons
# organiza isso 
gv = StringVar()
gv.set("")  # Valor padrão


label_gender = Label(frame1, text="Sexo: ", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 13, "bold"))
label_gender.place(x=50, y=90)

genders = ["masculino", "Feminino"]
rb_positions = [(120, 90), (220, 90)]  #(x,y) para cada radioButton

for i, (text, pos) in enumerate(zip(genders, rb_positions)):
    rb = Radiobutton(
        frame1,
        text=text,
        variable=gv,
        value=text,
        bg="#FFFFFF",
        font=('Helvetica', 12)
    )
    rb.place(x=pos[0], y=pos[1])





# Combobox//optionmenu
materias = ["História", "Português", "Geografia", "Matemática"]
mv = StringVar()
mv.set("Disciplina")

label_menu = Label(frame1, text="Selecione sua matéria", anchor=NW, fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14))
label_menu.place(x=50, y=127)

select_opt = ttk.Combobox(
    frame1,
    textvariable=mv,
    values=materias,
    state="readonly",
    font=('Helvetica', 14),
    style='TCombobox'
)
select_opt.place(x=50, y=160, width=273, height=35)



#botoes
#editar depois 
botao_inserir = Button(frame4,width=15, height=1, text="Gerar Relatório",anchor=CENTER,fg="#FFFFFF", bg="#00BF62",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_inserir.place(x=110, y=40) 


botao_apagar = Button(frame4,width=29, height=1, text="Cadastrar Novo Professor Substituto",anchor=CENTER,fg="#FFFFFF", bg="#FF3131",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_apagar.place(x=290, y=40) 


botao_atualizar = Button(frame1,width=13, height=2, text="Aplicar Filtro",anchor=CENTER,fg="#FFFFFF", bg="#5372FF",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_atualizar.place(x=130, y=400)



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



#tabela de verificação

check_vars = [[IntVar() for _ in range(6)] for _ in range(3)]

#cabeçalhos
Label(frame5, text="Disponibilidade", font=('Arial', 14)).grid(row=0, column=0, columnspan=7)
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
for i, dia in enumerate(dias, 1):
    Label(frame5, text=dia).grid(row=1, column=i)

#checkbuttons
periodos = ['Manhã', 'Tarde', 'Noite']
for row, periodo in enumerate(periodos, 2):
    Label(frame5, text=periodo).grid(row=row, column=0)
    for col in range(1, 7):
        Checkbutton(frame5, variable=check_vars[row-2][col-1],
                   onvalue=1, offvalue=0).grid(row=row, column=col)








janela.mainloop()      
