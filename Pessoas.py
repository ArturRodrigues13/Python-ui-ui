class pessoa:

	def __init__(self, nome: str, sobrenome: str, ocupacao: str, idade: int):
		self.nome = nome
		self.sobrenome = sobrenome
		self.ocupacao = ocupacao
		self.idade = idade

	def pegar_primeiro_nome(self) -> str:
		return self.nome

	def set_primeiro_nome(self, novo_primeiro_nome: str):
		self.nome = novo_primeiro_nome

	def pegar_sobrenome(self) -> str:
		return self.sobrenome

	def set_sobrenome(self, novo_sobrenome: str):
		self.sobrenome = novo_sobrenome

	def pegar_ocupacao(self) -> str:
		return self.ocupacao

	def set_ocupacao(self, novo_ocupacao: str):
		self.ocupacao = novo_ocupacao

	def pegar_idade(self) -> int:
		return self.idade

	def set_idade(self, novo_idade: int):
		self.idade = novo_idade

	def printa(self):
		print("Alou, meu nome é {} {}.".format(self.nome,self.sobrenome))
		print("Meu trabalho é {}.".format(self.ocupacao))
		print("Eu tenho {} anos.".format(self.idade))

def main():
	nome: str
	sobrenome: str
	ocupacao: str
	idade: int

	nome = input("Qual seu nome?")

	sobrenome = input("Qual seu sobrenome?")

	ocupacao = input("Trabalha com o que?")

	idade = int(input("E tem quantos aninhos o bebê"))

	eu = pessoa(nome,sobrenome,ocupacao,idade)

	eu.printa()

main()
