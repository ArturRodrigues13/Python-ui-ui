	# Versão Final (?): Bem simples, ele inverte o texto que o usuário
	# digita, apenas isso, eu só fiz isso pra fazer uma review do álbum
	# da Charli XCX, tamos juntos!!!

def inversor(lista: list):

	lista_nova = []

	for x in range(len(lista) - 1,-1,-1):
		lista_nova.append(lista[x])

	texto_final = "".join(lista_nova)

	return texto_final

def main():
	print("Opa, eai cabra, me vê o texto que você quer inverter aí")
	lista = list(input("Texto: "))

	print("\nManeiro, tá aí teu texto invertido, use com sabedoria: ")
	print(inversor(lista))

main()
