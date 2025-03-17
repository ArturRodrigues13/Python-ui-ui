def fatorial(n):
	# Caso Base: fatorial(0) = 1
	if n == 0:
		return 1
	else:
		# Caso Recursivo: fatorial(n) = n * fatorial(n - 1)
		return n * fatorial(n - 1)

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def soma(n):
	if n == 0:
		return 0
	else:
		return n + soma(n - 1)

def main():

	print("Olá, vamos fazer brincadeiras recursivas, primeiro, me dê um número qualquer para eu calcular seu fatorial")

	num = int(input())

	resultado = fatorial(num)

	print(f"Fatorial de {num} é {resultado}")

	print("Bacana, agora me dá outro número para eu calcular o Fibonacci dele")

	num = int(input())

	resultado = fibonacci(num)

	print(f"Fibonacci de {num} é {resultado}")

	print("Agora mais um pra eu calcular a soma de de 0 até esse número")

	num = int(input())

	resultado = soma(num)

	print(f"A soma de todos os termos de 0 até {num} é {resultado}")


main()
