import random

# Print básico
# print("Oi Mundo!!!")

# Print com umas somas no meio
# print(5 + 5, 10*20)

# if bem básico
if 6 > 2:
	print("uau")
else:
	print("baguga")

# Definição de variáveis, sem definir o tipo
x = 10

y = "parábens!"

z = 100.5

# Print dos tipos das variáveis
# print(type(x))
# print(type(y))
# print(type(z))

# Criação de lista
frutas = ["Maça", "Banana", "Uva"]

# atribuindo a cada variável um valor da lista, na ordem que tá escrito
x,y,z = frutas

# print(x)
# print(y)
# print(z)

# Função básica
def teste():
	# variável global, nesse caso eu tô editando o x que eu criei antes, se não colocasse o global eu ia editar um x local novo
	global x
	x = "casca"
	print(x + y + z)

teste()

string = "papin"

# Loop For simples (odeio essa versão)
for i in string:
	print(i)

# Print do tamanho da string, mas pode só do tamanho de uma lista também
# print(len(string))

string = "oiê, Teste Bacana bacanudo aqui pra ver se tem certa palavra nessa string uau"

# If simples com uma checagem mais específica
if "joão" in string:
	print("joão tá aqui")
elif "oiê" in string:
	print("oiê tá aqui")

# Not in, o oposto do que tá aí em cima
if "joão" not in string:
	print("joão não tá aqui")

# Print de apenas um certo número de caracteres, ou seja, vai printar o caractere 5 em diante até o 10 (não o 11, isso tinha me confundido um pouco antes)
# print(string[5:11])

# Printar com letras maiúsculas
# print(string.upper())

# Printar com letrar minúsculas
# print(string.lower())

# Substituir certa palavra com outra
# print(string.replace("oiê","caos"))

# Printar a string separando ela em pequenas partes quando encontrar um certo elemento
# print(string.split(" "))

idade = 19
money = 10.372365
# string especial pra adicionar variáveis no meio
txt = f"eu sou Artur e tenho {idade} anos, sou pobre e só tenho {money:.2f} reais na conta"
print(txt)

# Printar quanto de um certo elemento tem na string, nesse caso quantos letras a
print(string.count("a"))


lista = ["caps", "shift", "backspace", "tab"]

# Inserir um certo elemento em uma certa posição
lista.insert(0,"enter")

# Criar um elemento no final da lista
lista.append("alt")

# Aumentar uma lista colocando outra no final dela
lista.extend(frutas)

# Remover um certo elemento da lista
lista.remove("caps")

# Remover o elemento na posição x
lista.pop(2)

# Se usar sem argumento remove o último elemento da lista
lista.pop()

# Também remove um elemento específico
del lista[0]

print(lista)

# Deleta a lista, manda pro limbo
del lista

# Limpa a lista
frutas.clear()

print(frutas)

casas = ["nein", "nain", "num","nananinanao","oi"]

# Mais loops
for i in range(len(casas)):
  print(casas[i])

i = 0

while i < len(casas):
  print(casas[i])
  i = i + 1


# newlist = [expression for item in iterable if condition == True] <- sintaxe
babu = [x.upper() for x in casas if "n" in x]
# Nesse caso, a lista nova vai ser preenchida com os elementos em 'casas' que tiver a letra 'n' no meio, em letras maiúsculas porque eu especifiquei isso

print(babu)

# adiciona números menores que 5 a lista nova
matematica = [x for x in range(10) if x < 5]

print(matematica)

# Cria uma lista nova a partir da outra criada acima, se tiver um 3 no meio o elemento vira 10000, se não, continua normal
matematica2 = [x if x != 3 else 10000 for x in matematica]

print(matematica2)

# Organizar em ordem alfabetica normal
babu.sort()
# Organizar em ordem reversa, no caso decrescente porque aqui são números né
matematica2.sort(reverse = True)

print(babu)
print(matematica2)

# Função pra ele organizar em ordem de número mais próximo de 50
def maispertode50(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

# Definir isso que eu falei acima
thislist.sort(key = maispertode50)

print(thislist)

# Inverter a lista
babu.reverse()

print(babu)

# Duas formas diferentes de copiar uma lista
babu2 = babu.copy()

babu3 = list(babu)

print(babu2)
print(babu3)

# Juntar duas listas
babu4 = babu2 + babu3

print(babu4)

# Juntar duas listas também
for x in babu2:
	babu3.append(x)

print(babu3)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()		Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Notar a diferença na criação de tuplas () e listas []
# Tuplas são imutáveis, uma vez criada, nada pode ser modificado
mytuple = ("apple", "banana", "cherry")

print(mytuple)

# Para fazer uma tupla de 1 só item, tem que colocar uma vírgula assim
thistuple = ("apple",)

# As mesmas coisas que faziamos com listas, como checar tamanho, printar os elementos e etc continuam as mesmas aqui.

# Não podemos modificar tuplas, mas podemos converter elas em uma lista, mudar, e aí transformar em Tupla de novo

tuplechanger = list(mytuple)

tuplechanger.append("casual")

mytuple = tuple(tuplechanger)

print(mytuple)

# Dá pra somar tuplas também

mytuple += thistuple

print(mytuple)

# Da pra deletar a tupla também

# del thistuple

# tem como desempacotar as tuplas em variáveis, se quiser dá até pra transformar certas variáveis em uma lista

(var1,*var2,var3) = mytuple

print(var1,var2,var3)

# isso é muito bacana, é legal porque você pode usar o * pra controlar qual variável vira uma lista

# dá pra multiplicar tuplas também

mytuple *= 2

print(mytuple)

# sets não são mutáveis, não aceitam duplicatas (os dois acima aceitavam) e não tem uma ordem especifica, você pode adicionar e remover itens

myset = {"apple", "banana", "cherry"}

# eles não terem ordem significa que cada vez que tu usar eles, a ordem vai ser diferente, e você não pode pedir um index especifico (como que usa isso????)

# dá pra printar itens especificos usando uma checagem com 'in' ou outros condicionais

for x in myset:
	if x != "banana": print(x)

# dá pra usar funcões de add e update para adicionar itens no set, se quiser tirar um item use remove ou discard (remove dá erro se o item não existir, discard não)

# se usar pop() ele remove um item aleatório, dá pra usar clear e del pra fazer a mesma coisa que fazia com os outros acima

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset2 = set1.union(set2, set3, set4)
print(myset2)

