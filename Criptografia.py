def main():

	# Versão Beta, achei divertido, obviamente não tá totalmente desenvolvido porque esse código só aceita letras minúsculas e sem acento, vou fazer uma versão melhorada depois.

	alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	criptografia = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

	palavra = list(input())
	palavra_2 = palavra.copy()

	for x in range(len(palavra)):
		if palavra[x] in alfabeto:
			indice = alfabeto.index(palavra[x])
			palavra_2[x] = criptografia[indice]

	print(palavra_2)

main()
