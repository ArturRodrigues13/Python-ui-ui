def soma(a,b):
	return a + b

def subtracao(a,b):
	return a - b

def multiplicacao(a,b):
	return a * b

def divisao(a,b):
	if b == 0:
		print("Em uma divisão, o divisor não pode ser 0, não será possível executar essa operação")
		exit()
	return a / b

def main():
	print("Oieee, bem vindo a calculadora básica em python haha, me dá os números que tu quer calcular aí")

	num1 = int(input())
	num2 = int(input())

	print("""Beleuza, agora me diz qual operação tu quer calcular
	1 pra adição
	2 pra subtração
	3 pra multiplicação
	4 pra divisão""")

	operacao = int(input())

	if operacao == 1:
		resultado = soma(num1,num2)
	elif operacao == 2:
		resultado = subtracao(num1,num2)
	elif operacao == 3:
		resultado = multiplicacao(num1,num2)
	elif operacao == 4:
		resultado = divisao(num1,num2)
	else:
		print("Operação Inválida")
		return 1

	print(f"O resultado é {resultado:.2f}")

	return 0

main()
