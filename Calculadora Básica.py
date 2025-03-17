def calcula(a,b,operacao):
	resultado = 0
	if operacao == 1:
		resultado = a + b
	elif operacao == 2:
		resultado = a - b
	elif operacao == 3:
		resultado = a * b
	else:
		resultado = a / b

	return resultado

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

	resultado = calcula(num1,num2,operacao)

	print(f"O resultado é {resultado:.2f}")

	return 0

main()
