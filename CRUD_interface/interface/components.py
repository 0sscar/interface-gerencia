from tkinter import* 
from tkinter import ttk   


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

def radiobutton_genre(container, x_label, y_label, x_inicial_rb, y_rb, var=None, bg_color=None):

    bg_color = bg_color if bg_color else container.cget('bg')
    
    gv = var if var else StringVar()
    
    # Label "Sexo" com a cor de fundo
    Label(container, 
          text="Sexo: ", 
          anchor=NW, 
          font=('Helvetica', 13, "bold"),
          bg=bg_color).place(x=x_label, y=y_label)
    
    # Opções e RadioButtons
    genders = ["masculino", "Feminino"]
    for i, text in enumerate(genders):
        Radiobutton(
            container,
            text=text,
            variable=gv,
            value=text,
            font=('Helvetica', 12),
            bg=bg_color,  # Cor de fundo herdada
            activebackground=bg_color  # Cor quando ativo
        ).place(x=x_inicial_rb + (i * 100), y=y_rb)
    
    return gv

def combobox_materias(container, x, y, width=273, height=35):
   
    # Label acima do Combobox
    style = ttk.Style()
    
    # Variável e Combobox
    mv = StringVar()
    mv.set("Disciplina")
        # Estilo para estado normal
    style.configure('TCombobox',
        foreground='#A9A9A9',  # Cor do texto inicial (cinza)
        font=('Helvetica', 10),
        fieldbackground='white'
    )
    materias = ["História", "Português", "Geografia", "Matemática", "Biologia","Química","Inglês","Ed.Física", "Artes"]
    
    combobox = ttk.Combobox(
        container,
        textvariable=mv,
        values=materias,
        state="readonly",
        font=('Helvetica', 14),
        style='TCombobox'
    )
    combobox.place(x=x, y=y, width=width, height=height)
    
    return combobox, mv 


def check_week(container, x=0, y=0, bg_color=None):
    """Cria tabela de disponibilidade semanal"""
    # Cria um frame para conter a tabela 
    # Se não for especificada, pega a cor do container
    bg_color = bg_color if bg_color else container.cget('bg')
    
    frame = Frame(container, bg=bg_color)
    frame.place(x=x, y=y)
    
    check_vars = [[IntVar() for _ in range(6)] for _ in range(3)]
    
    # Cabeçalhos
    Label(frame,width=19, text="Disponibilidade",bg="#CCCCCC", font=('Arial', 14)).grid(row=0, column=0, columnspan=7)
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    for i, dia in enumerate(dias, 1):
        Label(frame,bg=container.cget('bg'), text=dia).grid(row=1, column=i)
    
    # Checkbuttons
    periodos = ['Manhã', 'Tarde', 'Noite']
    for row, periodo in enumerate(periodos, 2):
        Label(frame, bg=container.cget('bg'),text=periodo).grid(row=row, column=0)
        for col in range(1, 7):
            Checkbutton(frame, 
                      variable=check_vars[row-2][col-1],
                      onvalue=1, 
                      bg=container.cget('bg'),
                      offvalue=0).grid(row=row, column=col)
                      
    return check_vars, frame  # Retorna tanto as variáveis quanto o frame





