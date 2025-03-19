import math

class FiguraGeometrica:
	def CalcularArea(self):
		pass
	def CalcularPerimetro(self):
		pass

class Circulo(FiguraGeometrica):
	def __init__(self, raio):
		self.raio = raio

	def CalcularArea(self):
		return math.pi * self.raio * self.raio

	def CalcularPerimetro(self):
		return 2 * math.pi * self.raio

class Quadrado(FiguraGeometrica):
	def __init__(self, lado):
		self.lado = lado

	def CalcularArea(self):
		return self.lado * self.lado

	def CalcularPerimetro(self):
		return self. lado * 4

class Retangulo(FiguraGeometrica):
	def __init__(self, base,altura):
		self.base = base
		self.altura = altura

	def CalcularArea(self):
		return self.base * self.altura

	def CalcularPerimetro(self):
		return (self.altura * 2) + (self.base * 2)

class Triangulo(FiguraGeometrica):
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def CalcularArea(self):
		return (self.base * self.altura) / 2

	def CalcularPerimetro(self):
		return self.base + 2 * (math.sqrt(math.pow(self.altura,2) + math.pow(self.base / 2,2)))

def main():

	print("Calculador de Área\n")
	print("1. Círculo\n")
	print("2. Quadrado\n")
	print("3. Retângulo\n")
	print("4. Triângulo\n")
	escolha = int(input("Escolha uma Figura: "))

	if (escolha == 1):
		raio = float(input("\nDigite o Raio do Círculo: "))
		figura = Circulo(raio)

	elif (escolha == 2):
		lado = float(input("Digite a medida de um dos lados do Quadrado: "))
		figura = Quadrado(lado)

	elif (escolha == 3):
		base = float(input("Digite a Base do Retangulo: "))
		altura = float(input("Digite a Altura do Retangulo: "))
		figura = Retangulo(base,altura)

	elif (escolha == 4):
		base = float(input("Digite a Base do Triângulo: "))
		altura = float(input("Digite a Altura do Triângulo: "))
		figura = Triangulo(base,altura)

	else:
		print("Opção Inválida, tente novamente.")
		exit()


	print(f"A área e o perímetro da figura escolhida são, respectivamente: {figura.CalcularArea():.2f} e {figura.CalcularPerimetro():.2f}")

main()
