x = [1,2,3,4,5]
y = [i**2 for i in x]

for i in x:
	y.append(i**2)

print(x)
print(y)

z = [i for i in x if i%2==1]

print(z)

# -----------------------------------------

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
	print(i, lista[i])

for i, nome in enumerate(lista):
	print(i, nome)

# -----------------------------------------

def dobro(x):
	return x*2

valor = [1,2,3,4,5]
print(dobro(valor))

valor_dobrado = map(dobro, valor)

print(list(valor_dobrado))

# ------------------------------------------

from functools import reduce

def soma(x,y):
	return x+y 

lista = [1,3,5,10,20]

soma = reduce(soma, lista)
print(soma)

# -------------------------------------------

lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$3,00", "R$5,00", "R$30,00", "R$80,00"]

for numero, nome in zip(lista1, lista2):
	print(numero, nome)

for numero, nome in zip(lista1, lista3):
	print(numero, nome)