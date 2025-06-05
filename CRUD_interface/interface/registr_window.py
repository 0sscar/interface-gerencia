from tkinter import* 
from tkinter import messagebox   
from components import check_week
from edit_regstr_window import editprofessor
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao,vermelho

def warning(dados_professor): 
    
    messagebox.askquestion("Confimação", f"Tem certeza que deseja apagar {dados_professor[1]} ?") 



def exibir_registro(dados_professor):
    janela_regstr = Toplevel()
    janela_regstr.title("Detalhes do Professor")
    janela_regstr.geometry("400x350")
    janela_regstr.configure(bg=verde)
    janela_regstr.resizable(width=FALSE, height=FALSE)
    janela_regstr.grab_set() 
      
    
    barra = Frame(janela_regstr, width = 410, height=40, bg=azul)
    barra.place(x=0, y=0) 

    tabela = Frame(janela_regstr,width=210, height=130,bg=cor_tabela) 
    tabela.place(x=90,y=120)
    # Labels com os valores usando place()
    Label(barra,anchor=NW,text="Professor:", font=('Helvetica', 12, 'bold'),bg=azul).place(x=39, y=9)
    
    Label(janela_regstr,text=dados_professor[1],font=('Helvetica', 12,'bold'),bg=azul).place(x=135, y=9)#variavel nome
    

    
    Label(janela_regstr, text="Disciplina:",font=('Helvetica', 12,'bold'),bg=verde).place(x=39, y=50)
    
    Label(janela_regstr, text=dados_professor[2],font=('Helvetica', 12,'bold'),bg=verde).place(x=135, y=50)
    




    # Botão de fechar
    Button(janela_regstr,text="Voltar",command=janela_regstr.destroy,font=('Helvetica', 11,'bold'),width=8,bg=cor_botao, fg="black").place(x=70, y=290) 

    Button(janela_regstr, text="Apagar",command=lambda:warning(dados_professor),font=('Helvetica', 11,'bold'),width=7,bg=vermelho, fg="white").place(x=160, y=290)

    Button(janela_regstr, text="Editar",command=lambda:editprofessor(dados_professor),font=('Helvetica', 11,'bold'),width=8,bg=verde_claro, fg="white").place(x=240, y=290)


    check_week(tabela)
    
    janela_regstr.mainloop() 





    

