def calcular_disponibilidade(check_vars) -> int:
	disponibilidade = 0
	for turno in range(3):
		for dia in range(6):
			valor = check_vars[turno][dia].get()
			if valor:
				disponibilidade += 1 << (3*dia + turno)
	return disponibilidade

def definir_check_vars(check_vars, disponibilidade: int) -> None:
	for turno in range(3):
		for dia in range(6):
			marcado = (disponibilidade & (1 << (3*dia + turno))) > 0
			check_vars[turno][dia].set(marcado)
