from tkinter import* 

janela = Tk() 
janela.geometry("1043x593")
janela.configure(bg="#0C0C0C")
janela.resizable(width=FALSE, height=FALSE)#janela fixa


#divisão de elementos 
frame1 = Frame(janela, width = 410, height=600, bg="#FFFFFF")
frame1.grid(row=0, column=0) 

frame2 = Frame(janela,width=640, height=600,bg="#C5C5C5", relief="flat")
frame2.grid(row=0, column=1)


label_nome = Label( frame1, text="Insira o nome do professor", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14)) 
label_nome.place(x=50, y=20) 

entry_nome = Entry(frame1, width=45, justify="left", relief="solid") 
entry_nome.place(x=50,y=50)

label_email = Label( frame1, text="Insira o email", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14)) 
label_email.place(x=50, y=90)

entry_email = Entry(frame1, width=45, justify="left", relief="solid") 
entry_email.place(x=50, y=120)

#criando o option menu 
materias= ["História", "Português","Geografia", "Matemática"]
mv= StringVar(janela)
mv.set("Disciplina") 

label_menu = Label( frame1, text="Selecione sua matéria", anchor=NW,fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14)) 
label_menu.place(x=50, y=160)

select_opt = OptionMenu(frame1, mv, *materias) 
select_opt.config( fg="#0C0C0C", bg="#FFFFFF", font=('Helvetica', 14),relief="flat")
select_opt.place(x=50, y=190, width=273, height=30)


botao_inserir = Button(frame1,width=10, height=1, text="Cadastrar",anchor=CENTER,fg="#FFFFFF", bg="#00BF62",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_inserir.place(x=50, y=540) 


botao_apagar = Button(frame1,width=10, height=1, text="Apagar",anchor=CENTER,fg="#FFFFFF", bg="#FF3131",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_apagar.place(x=155, y=540) 


botao_atualizar = Button(frame1,width=10, height=1, text="Atualizar",anchor=CENTER,fg="#FFFFFF", bg="#5372FF",font=("Ivy 10 bold"), relief= "raised", overrelief="ridge" )
botao_atualizar.place(x=260, y=540)
janela.mainloop()  