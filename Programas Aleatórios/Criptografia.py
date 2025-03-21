	# Versão Beta 2.0 : Okay, agora conseguimos lidar com letras maiúsculas e números na frase que vai ser codificada, além
	# de ter mudado a forma de armazenar a criptografia, usar dicionários é bem mais fácil. Mudanças futuras serão eu
	# comentar o código, que definitivamente tá faltando, e talvez achar uma forma melhor de lidar com caracteres especiais
	# nessa versão ele só ignora eles e traduz o resto normal, mas talvez uma abordagem mais sofisticada seja melhor.

def enigma(palavra: list,escolha: int):

	codificacao = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5','f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
	'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15','p': '16', 'q': '17', 'r': '18', 's': '19',
	't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25','z': '26', ' ' : '27', '-': '28',
	'_': '29', '.': '30', '!': '31', '?': '32',
	'1': 'A', '2': 'b', '3': 'C', '4': 'd', '5': 'E','6': 'f', '7': 'G', '8': 'h', '9': 'I', '0': 'j',
	}

	decodificacao = {v: k for k, v in codificacao.items()}

	'''
	alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	criptografia = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
	'''

	if escolha == 1:
		texto_codificado = []
		for caractere in palavra:
			texto_codificado.append(codificacao.get(caractere.lower(), caractere))
		texto_final = ' '.join(texto_codificado)
		print(texto_final)

	elif escolha == 2:
		texto_decodificado = []
		for caractere in palavra:
			texto_decodificado.append(decodificacao.get(caractere.lower(), caractere))
		texto_final = ''.join(texto_decodificado)
		print(texto_final)

def main():
	escolha = int(input("Codificar (1) ou decodificar (2)? "))

	if escolha == 1:
		palavra = list(input("Okay, me dê o conteúdo que vai ser codificado: "))
		enigma(palavra,1)

	elif escolha == 2:
		palavra = input("Okay, me dê o código que vai ser decodificado: ")
		lista = palavra.split(" ")
		enigma(lista,2)

	else:
		print("Escolha ERRADA!!!")
		exit()

main()
