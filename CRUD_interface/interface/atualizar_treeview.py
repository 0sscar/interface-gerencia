import backend
import re

def formatar_nome(texto: str) -> str:
	aux1 = texto.lower()
	aux2 = re.sub(r"[áàãâä]", "a", aux1)
	aux3 = re.sub(r"[éèẽêë]", "e", aux2)
	aux4 = re.sub(r"[íìĩîï]", "i", aux3)
	aux5 = re.sub(r"[óòõôö]", "o", aux4)
	aux6 = re.sub(r"[úùũûü]", "u", aux5)
	aux7 = aux6.replace("ç", "c").replace("ñ", "n")
	aux8 = re.sub(r"[^a-z0-9]", "", aux7)
	return aux8

def atualizar_treeview(treeview) -> None:
    for fileira in treeview.get_children():
        treeview.delete(fileira)

    professores = backend.query_profs()
    print(f"query de professores: {professores}")
    for professor in professores:
        treeview.insert("", "end", values=(professor[0], professor[2], professor[1], professor[3], professor[4]))

def atualizar_treeview_filtrada(treeview, nome="", sexo="", disciplina="", disponibilidade=-1) -> None:
	for fileira in treeview.get_children():
		treeview.delete(fileira)
	
	nome = formatar_nome(nome)
	sexo = sexo.upper()
	disciplina = disciplina.title()
	
	professores = backend.query_profs()
	#print(f"\n\natualizar_treeview_filtrada(): query de professores: {professores}")
	print(f"filtrando por nome={nome}, sexo={sexo}, disciplina={disciplina}, disponibilidade={disponibilidade}")
	for professor in professores:
		#print(f"professor[2].upper()={professor[2].upper()}, sexo=\"{sexo}\"")
		if sexo != "" and (professor[2].upper() != sexo): continue

		#print(f"professor[3].title()={professor[3].title()}, disciplina=\"{disciplina}\"")
		if disciplina != "" and (professor[3].title() != disciplina): continue

		#print(f"formatar_nome(professor[1])={formatar_nome(professor[1])}, nome=\"{nome}\"")
		if nome != "" and (not formatar_nome(professor[1]).startswith(nome)): continue

		#print(f"disponibilidade & professor[4]={disponibilidade & professor[4]}, disponibilidade=\"{disponibilidade}\"")
		if disponibilidade != -1 and (disponibilidade & professor[4] != disponibilidade): continue

		treeview.insert("", "end", values=(professor[0], professor[2], professor[1], professor[3], professor[4]))
