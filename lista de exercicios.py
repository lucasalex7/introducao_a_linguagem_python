idade = int(input())

if idade >= 18:
	print("é maior de idade")
else:
	print("é menor de idade")

# -----------------------------------------

nota1 = int(input())
nota2 = int(input())

media = (nota1 + nota2) / 2

if media >= 6:
	print("aprovado")
else:
	print("reprovado")

# -----------------------------------------

import math

a = int(input())
b = int(input())
c = int(input())

x1 = (-b + math.sqrt((b**2) - (4*a*c)))/2*a 
x2 = (-b - math.sqrt((b**2) - (4*a*c)))/2*a 

print(x1, x2)

# ------------------------------------------

lista = [2, 8, 33]

ordem = lista.sort()

print(ordem)

# ------------------------------------------

n1 = float(input())
n2 = float(input())
sinal = input()

if sinal == "*":
	print(n1*n2)
elif sinal == "+":
	print(n1+n2)
elif sinal == "-":
	print(n1-n2)
else:
	print(n1/n2)

# -------------------------------------------