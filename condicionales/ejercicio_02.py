"""Algoritmo que pida un numero e indique si es positivo, 
negativo o 0"""

num=int(input("Ingresa el número: "))

if num==0:
	print("El número es igual a 0")
else:
	if num>0:
		print("El numero es positivo")
	else:
		print("El numero es negativo")
