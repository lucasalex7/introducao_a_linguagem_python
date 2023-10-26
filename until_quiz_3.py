import random

lista = [6, 45, 9]
numero = random.choice(lista)
print(numero)

# ------------------------------------------

a = 2
b = 0

try:
	print(a/b)

except:
	print("nao pode dividir por zero")