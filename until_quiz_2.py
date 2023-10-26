x = 1
y = 2

if x > y:
	print("x é maior que y")
elif y > x and y == 2: 
	print("y é igual a 2 e é maior que x")
else:
	print("y é maior que x")

# ---------------------------------------------------

while x < 10:
	print("x é maior que 10")
	print(x)
	x += x

# ---------------------------------------------------

lista = [1,2,3,4,5]
lista2= ["olá mundo", 4.5, 2, "greg", True]

for i in lista2:
	print(i)

# ----------------------------------------------------

for i in range(10):
	print(i)

for i in range(10,20,3):
	print(i)

# ----------------------------------------------------

a = "Lucas"
b = "Ribeiro"

concatenar = a + " " + b

print(concatenar)
print(a[1])
print(concatenar[0:6])

# ----------------------------------------------------

print(concatenar.lower())
print(concatenar.upper())
#----
concatenar2 = a + " " + b + "\n"
print(concatenar2)
print(concatenar2.strip())
#----
ditado = "O rato roeu a roupa do rei de roma"
print(ditado)
ditado2 = ditado.split(" ")
print(ditado2)
#----
busca = ditado.find("rei")
print(busca)

diferente = ditado.replace("o rei", "a rainha")
print(diferente)

# ---------------------------------------------------

def soma(x,y):
	print(x+y)

soma(3, 5)

def multiplicacao(x,y):
	return x*y 

print(multiplicacao(4,8))

# ---------------------------------------------------

arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

print(linhas)

for linha in linhas:
	print(linha)

w = open("arquivo2.txt", "a")

w.write("Esse é o meu arquivo")

w.close()

# ---------------------------------------------------

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 67.88, False]

print(minha_lista[2])

for item in minha_lista:
	print(item)

tamanho = len(minha_lista)

print(tamanho)

minha_lista.append("limao")

print(minha_lista)

if 7 in minha_lista2:
	print("7 está na lista")
else:
	print("7 não esta na lista")

del minha_lista[2:]
print(minha_lista)

minha_lista4 = []

minha_lista4.append(58)
print(minha_lista4)

# --------------------------------------------------

lista = [137, 669, 45, 34, 1, 9]
lista.sort()

a = lista.sort(reverse=True)

print(lista)
print(a)

lista5 = ["bola", "abacate", "dinheiro"]
lista5.sort()

print(lista5)

# --------------------------------------------------

meu_dicionario = {"A": "Ameixa", "B":"Bola", "C":"Cachorro"}

print(meu_dicionario["A"])

for chave in meu_dicionario:
	print(meu_dicionario[chave])

print(meu_dicionario.items())