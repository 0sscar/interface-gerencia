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

def radiobutton_genre(container, x_label, y_label, x_inicial_rb, y_rb):
    """
    Cria um grupo de RadioButtons para seleção de gênero
    
    Args:
        container: O frame ou janela onde será colocado
        x_label, y_label: Posição do label "Sexo"
        x_inicial_rb: Posição X inicial dos RadioButtons
        y_rb: Posição Y dos RadioButtons
        
    Returns:
        StringVar: Variável que armazena a seleção
    """
    gv = StringVar()
    gv.set("")
    
    # Label "Sexo"
    Label(
        container,
        text="Sexo: ",
        anchor=NW,
        fg="#0C0C0C",
        bg="#FFFFFF",
        font=('Helvetica', 13, "bold")
    ).place(x=x_label, y=y_label)
    
    # Opções e RadioButtons
    genders = ["masculino", "Feminino"]
    for i, text in enumerate(genders):
        Radiobutton(
            container,
            text=text,
            variable=gv,
            value=text,
            bg="#FFFFFF",
            font=('Helvetica', 12)
        ).place(x=x_inicial_rb + (i * 100), y=y_rb)
    
    return gv

def combobox_materias(container, x, y, width=273, height=35):
    """
    Cria um Combobox para seleção de matérias
    
    Args:
        container: O frame ou janela onde será colocado
        x, y: Posição do componente
        width: Largura do Combobox
        height: Altura do Combobox
        
    Returns:
        tuple: (Combobox, StringVar) para controle
    """
    # Label acima do Combobox
    Label(
        container,
        text="Selecione sua matéria",
        anchor=NW,
        fg="#0C0C0C",
        bg="#FFFFFF",
        font=('Helvetica', 14)
    ).place(x=x, y=y-33)  # 33 pixels acima do Combobox
    
    # Variável e Combobox
    mv = StringVar()
    mv.set("Disciplina")
    
    materias = ["História", "Português", "Geografia", "Matemática", "Biologia","Química","Ed.Física", "Artes"]
    
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



