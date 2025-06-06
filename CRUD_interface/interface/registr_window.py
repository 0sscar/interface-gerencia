from tkinter import* 
from tkinter import messagebox   
from components import check_week
from edit_regstr_window import editprofessor
from cores import azul, verde,branco,verde_claro,cor_tabela,cor_botao,vermelho
import backend
from disponibilidade import calcular_disponibilidade, definir_check_vars
from atualizar_treeview import atualizar_treeview


def exibir_registro(treeview, dados_professor):
    janela_regstr = Toplevel()
    janela_regstr.title("Detalhes do Professor")
    janela_regstr.geometry("400x350")
    janela_regstr.configure(bg=verde)
    janela_regstr.resizable(width=FALSE, height=FALSE)
    janela_regstr.wait_visibility()
    janela_regstr.grab_set()


    variaveis = {
        "id": IntVar(value=int(dados_professor[0])),
        "sexo": StringVar(value=dados_professor[1]),
        "nome": StringVar(value=dados_professor[2]),
        "disciplina": StringVar(value=dados_professor[3]),
        "disponibilidade": IntVar(value=int(dados_professor[4])),
    }
      
    
    barra = Frame(janela_regstr, width = 410, height=40, bg=azul)
    barra.place(x=0, y=0) 

    tabela = Frame(janela_regstr,width=210, height=130,bg=cor_tabela) 
    tabela.place(x=90,y=120)

    # Labels com os valores usando place()
    Label(barra,anchor=NW,text="Professor:", font=('Helvetica', 12, 'bold'),bg=azul).place(x=39, y=9)
    Label(janela_regstr,textvariable=variaveis["nome"],font=('Helvetica', 12,'bold'),bg=azul).place(x=135, y=9)#variavel nome


    Label(janela_regstr, text="Disciplina:",font=('Helvetica', 12,'bold'),bg=verde).place(x=39, y=50)
    Label(janela_regstr, textvariable=variaveis["disciplina"],font=('Helvetica', 12,'bold'),bg=verde).place(x=135, y=50)


    check_vars, _ = check_week(tabela, disponibilidade=variaveis["disponibilidade"].get(), disabled=True)
    variaveis["check_vars"] = check_vars
    

    def warning(dados_professor):
        apagar = messagebox.askyesno("Apagar Cadastro", f"Tem certeza que deseja apagar o cadastro de {variaveis["nome"].get()}?")
        if apagar:
            backend.deletar_prof(variaveis["id"].get())
            messagebox.showinfo("Apagar Cadastro", f"Cadastro de {variaveis["nome"].get()} apagado com sucesso.")
            janela_regstr.destroy()
            atualizar_treeview(treeview)



    # Botão de fechar
    Button(janela_regstr,text="Voltar",command=janela_regstr.destroy,font=('Helvetica', 11,'bold'),width=8,bg=cor_botao, fg="black").place(x=70, y=290) 

    Button(janela_regstr, text="Apagar",command=lambda:warning(dados_professor),font=('Helvetica', 11,'bold'),width=7,bg=vermelho, fg="white").place(x=160, y=290)

    Button(janela_regstr, text="Editar",command=lambda:editprofessor(treeview, variaveis, dados_professor),font=('Helvetica', 11,'bold'),width=8,bg=verde_claro, fg="white").place(x=240, y=290)
    
    janela_regstr.mainloop() 




    

