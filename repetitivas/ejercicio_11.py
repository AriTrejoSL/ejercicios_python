"""Escribe un programa que diga si un número introducido 
por teclado es o no primo. 
//Un número primo es aquel que sólo es divisible entre él 
mismo y la unidad. 
//Nota: Es suficiente probar hasta la raíz cuadrada del 
número para ver si es 
//divisible por algún otro número."""

import math

numPrimo=int(input("Ingresa un número para ver si es primo: "))
esPrimo=True

for num in range(2, int(math.sqrt(numPrimo))+1):
	if numPrimo%num==0:
		esPrimo=False
		break
if esPrimo and numPrimo>1:
	print("Es primo")
else:
	print("No es primo")


