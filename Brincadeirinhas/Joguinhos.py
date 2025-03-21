	# Versão Beta: Foi bem legal fazer isso, obviamente tá longe de estar finalizado, vou adicionar um menu e também
	# Outros mini joguinhos, talvez um jogo da velha, coisas assim (além de enfeitar e deixar o código bonito!!!)

import random

def adivinhe():
	tentativas = 1
	ganhou = False
	diferenca = 0
	print("Olá, bem vindo ao jogo Adivinhe o Número!!!")
	print("Primeiramente, escolha o nível de dificuldade:")
	print("1.Fácil: Adivinhar entre 0 e 50")
	print("2.Médio: Adivinhar entre 0 e 100")
	print("3.Difícil: Adivinhar entre 0 e 300")
	print("4.Muito Difícil: Adivinhar entre 0 e 1000")
	print("5.Impossível: Adivinhar entre 0 e 5000")

	print("Caso queira voltar para o menu, digite 0")
	dificuldade = int(input())

	if(dificuldade == 0):
		return 0
	elif dificuldade == 1:
		numero_adivinhar = random.randint(0,50)
	elif dificuldade == 2:
		numero_adivinhar = random.randint(0,100)
	elif dificuldade == 3:
		numero_adivinhar = random.randint(0,300)
	elif dificuldade == 4:
		numero_adivinhar = random.randint(0,1000)
	elif dificuldade == 5:
		numero_adivinhar = random.randint(0,5000)

	chute = int(input("Muito bem, agora vamos começar o jogo, chute um número aí: "))

	while ganhou == False:
		print(f"\nTentativa atual: {tentativas}")

		if chute > numero_adivinhar:
			diferenca = chute - numero_adivinhar
		elif chute < numero_adivinhar:
			diferenca = numero_adivinhar - chute
		elif chute == numero_adivinhar:
			print("\nACERTOU MISERAVIIII")
			ganhou = True
			break

		if diferenca <= 3:
			print("\nTÁ FERVENDOOO, NA BOCA DO VULCÃO")
		elif diferenca > 3 and diferenca <= 10:
			print("\nTá quente, tá faltando pouco pô")
		elif diferenca > 10 and diferenca <= 30:
			print("\nTá morno, tá indo no caminho certo")
		elif diferenca > 30 and diferenca < 100:
			print("\nTá frio frio frio, mas poderia ser pior")
		else:
			print("\nVocê está na artártida amigo, tenta melhor aí")

		tentativas += 1

		chute = int(input("\nOkay, tente mais uma vez aí: "))

	print(f"\nBOA DOG, ACERTOU O NÚMERO {numero_adivinhar} EM {tentativas} TENTATIVAS, LESGOOOOO")
	return 0



def main():
	numero = int(input())

	if numero == 1:
		adivinhe()

	return 0

main()
