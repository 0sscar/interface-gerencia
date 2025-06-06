import sqlite3
from datetime import datetime

NOME_BANCO = "banco.sqlite"
NOME_RELATORIOS = "relatorios.txt"

#ALFABETO = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# embaralhei o alfabeto porque há casos como "senha" --> "aSENHA".
# embaralhar deixa mais aleatório.
ALFABETO = "VeuUA8QyitkRP7BTHnO5o3ED1gGZ0mWwd4qrvjc2KpIFaxhJzM6YNL9fCSsblX"

def criptografarSenha(senha_bruta: str) -> str:
	"""Criptografia: [senha_bruta] --> [chave][senha_criptografada].

	A chave é um caractere, representando um valor numérico para a cifra de César.
	
	Não precisava, mas implementei isso a fins de aprendizado."""

	# a chave é a soma de todos os caracteres.
	# caracteres fora do ALFABETO valem 29, porque sim.
	chave = 0
	for char in senha_bruta:
		if char in ALFABETO:
			chave += ALFABETO.index(char)
		else:
			chave += 29
	chave = chave % len(ALFABETO)
	# se a chave for 0, ele guarda a senha original, então é bom mudar antes
	chave = 29 if chave == 0 else chave

	# aplica cifra de César
	senha_criptografada = ALFABETO[chave]
	for char in senha_bruta:
		if char in ALFABETO:
			senha_criptografada += ALFABETO[(ALFABETO.index(char)+chave) % len(ALFABETO)]
		else:
			senha_criptografada += char
	
	print(f"criptografarSenha(\"{senha_bruta}\") -> \"{senha_criptografada}\"")
	return senha_criptografada



def relatar(mensagem: str) -> None:
	# força a criação do arquivo.
	try:
		with open(NOME_RELATORIOS, "x") as arq: pass
	except FileExistsError:
		pass

	with open(NOME_RELATORIOS, "a") as arq:
		data = datetime.today().strftime("[%Y/%m/%d %H:%M:%S]")
		arq.write(f"{data} {mensagem}\n")



def conectar_banco():
	return sqlite3.connect(NOME_BANCO)

def criar_tabelas() -> None:
	conn = conectar_banco()
	conn.executescript("""
		CREATE TABLE IF NOT EXISTS Administradores (
			nome TEXT PRIMARY KEY,
			senha TEXT
		);

		CREATE TABLE IF NOT EXISTS Professores (
			id INTEGER PRIMARY KEY,
			nome TEXT NOT NULL,
			sexo CHAR(1) NOT NULL,
			disciplina TEXT NOT NULL,
			disponibilidade INTEGER NOT NULL
		);
	""")
	conn.commit()
	conn.close()
	relatar("Tabelas criadas com sucesso.")

def query_adm():
	conn = conectar_banco()
	cursor = conn.execute("""
		SELECT * FROM Administradores;
	""")
	query = cursor.fetchall()
	cursor.close()
	conn.close()
	return query

def existe_adm(nome: str) -> bool:
	"""Checa se o(a) Administrador(a) `nome` existe no banco."""
	nome = nome.title()

	conn = conectar_banco()
	cursor = conn.execute("""
		SELECT nome FROM Administradores WHERE nome=?;
	""", (nome,))
	query = cursor.fetchone()
	cursor.close()
	conn.close()
	return query != None

def criar_adm(nome: str, senha_bruta: str) -> None:
	"""Emite exceção se `nome` já existir."""
	nome = nome.title()

	conn = conectar_banco()
	conn.execute("""
		INSERT INTO Administradores (nome,senha) VALUES (?,?);
	""", (nome, criptografarSenha(senha_bruta)))
	conn.commit()
	conn.close()
	relatar(f"Administrador(a) \"{nome}\" registrado(a) com sucesso.")

def logar_adm(nome: str, senha_bruta: str) -> bool:
	"""Retorna `True` se as credenciais forem válidas."""
	nome = nome.title()

	conn = conectar_banco()
	cursor = conn.execute("""
		SELECT nome FROM Administradores WHERE nome=? AND senha=?;
	""", (nome, criptografarSenha(senha_bruta)))
	query = cursor.fetchone()
	cursor.close()
	conn.close()
	relatar(f"Login de \"{nome}\" efetuado com sucesso!")
	return query != None


# [TO-DO] talvez seja bom fazer uma classe Professor e mover as validações pra lá?
def criar_prof(nome: str, sexo: str, disciplina: str, disponibilidade: int) -> None:
	"""Emite `ValueError` se:
	- `sexo` for diferente de \"M\" ou \"F\";
	- `disponibilidade < 0 (nenhum dia marcado) e > 262143 (todos marcados).`"""

	nome = nome.title()
	sexo = sexo.upper()
	disciplina = disciplina.title()

	if sexo != "M" and sexo != "F":
		raise ValueError(f"sexo deve ser \"M\" ou \"F\", recebido \"{sexo}\".")
	elif disponibilidade < 0 or disponibilidade > 262143:
		raise ValueError(f"disponibilidade deve ser >= 0 e <= 262143, recebido {disponibilidade}.")

	conn = conectar_banco()
	conn.execute("""
		INSERT INTO Professores (nome, sexo, disciplina, disponibilidade) VALUES (?, ?, ?, ?)
	""", (nome, sexo, disciplina, disponibilidade))
	conn.commit()
	conn.close()
	relatar(f"Professor(a) \"{nome}\" registrado(a) com sucesso.")

def atualizar_prof(id: int, nome: str, sexo: str, disciplina: str, disponibilidade: int) -> None:
	"""Emite `ValueError` se:
	- `sexo` for diferente de \"M\" ou \"F\";
	- `disponibilidade < 0 (nenhum dia marcado) e > 262143 (todos marcados).`"""

	nome = nome.title()
	sexo = sexo.upper()
	disciplina = disciplina.title()

	if sexo != "M" and sexo != "F":
		raise ValueError(f"sexo deve ser \"M\" ou \"F\", recebido \"{sexo}\".")
	elif disponibilidade < 0 or disponibilidade > 262143:
		raise ValueError(f"disponibilidade deve ser >= 0 e <= 262143, recebido {disponibilidade}.")

	conn = conectar_banco()
	conn.execute("""
		UPDATE Professores SET nome=?, sexo=?, disciplina=?, disponibilidade=? WHERE id=?
	""", (nome, sexo, disciplina, disponibilidade, id))
	conn.commit()
	conn.close()
	relatar(f"Registro do(a) Professor(a) \"{nome}\" foi atualizado com sucesso.")

def deletar_prof(id: int) -> None:
	conn = conectar_banco()
	conn.execute("""
		DELETE FROM Professores WHERE id=?
	""", (id,))
	conn.commit()
	conn.close()
	relatar(f"Registro do(a) Professor(a) com ID {id} foi apagado do sistema.")

def query_profs():
	conn = conectar_banco()
	cursor = conn.execute("""
		SELECT * FROM Professores;
	""")
	query = cursor.fetchall()
	cursor.close()
	conn.close()
	return query

def query_prof(id: int):
	conn = conectar_banco()
	cursor = conn.execute("""
		SELECT * FROM Professores WHERE id=?;
	""", (id,))
	query = cursor.fetchall()
	cursor.close()
	conn.close()
	return query

# o filtro é realizado no front-end
#def query_prof_filtros(nome="", sexo="", disciplina="", disponibilidade=-1):
#	"""O filtro de nome busca por registros que começam com tal string."""
#	nome = nome.title()
#	sexo = sexo.upper()
#	disciplina = disciplina.title()
#
#	filtros_sql = []
#	filtros_dados = []
#	if nome != "":
#		filtros_sql.append("nome LIKE ?")
#		filtros_dados.append(nome + "%")
#	if sexo != "":
#		filtros_sql.append("sexo=?")
#		filtros_dados.append(sexo)
#	if disciplina != "":
#		filtros_sql.append("disciplina=?")
#		filtros_dados.append(disciplina)
#	if disponibilidade != -1:
#		filtros_sql.append("disponibilidade=?")
#		filtros_dados.append(disponibilidade)
#
#	conn = conectar_banco()
#	cursor = conn.execute(f"""
#		SELECT * FROM Professores{" WHERE " if len(filtros_sql) > 0 else ""}{" AND ".join(filtros_sql)};
#	""", tuple(filtros_dados))
#	query = cursor.fetchall()
#	cursor.close()
#	conn.close()
#	return query



if __name__ != "__main__":
	criar_tabelas()
	conn = conectar_banco()
#	conn.execute("""
#		DELETE FROM Administradores;
#	""")
#	conn.execute("""
#		DELETE FROM Professores;
#	""")
	conn.commit()
	conn.close()



#def main() -> None:
#	criar_tabelas()
#
#	conn = conectar_banco()
#	conn.execute("""
#		DELETE FROM Administradores;
#	""")
#	conn.execute("""
#		DELETE FROM Professores;
#	""")
#	conn.commit()
#	conn.close()
#
#	criar_adm("Raphael", "1234")
#	print(query_adm())
#	print(logar_adm("Raphael", "1234"))
#
#	criar_prof("Gervásio Mendes", "M", "Língua Portuguesa", 455)
#	criar_prof("Lídia Nunes", "F", "Língua Portuguesa", 56)
#	criar_prof("Paulo", "M", "Educação Física", 7)
#	criar_prof("Patrick", "M", "Educação Física", 56)
#	criar_prof("Pâmela", "F", "Educação Física", 7)
#	print(query_prof())
#	atualizar_prof(2, "Lídia", "F", "Matemática", 15)
#	print(query_prof())
#	deletar_prof(2)
#	print(query_prof())
#
#	print("\n\nquery com filtro:")
#	print(query_prof_filtros(disponibilidade=56, sexo="f"))
#
#
#
#if __name__ == "__main__":
#	main()
#else:
#	print(f"Rode este programa com python {__file__}")
