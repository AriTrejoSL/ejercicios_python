"""Crea un numero que permita adivinar u número, La aplicación 
genera un número aleatorio del 1 al 100."""

print("Adivina el número")
import random
intentos=0

numero_es=random.randint(1, 100)

while intentos <10:
	numero=int(input("Ingresa un número para adivinar: "))
	intentos=intentos+1
	if numero_es==numero:
		print("Adivinaste")
		#print(f"Fueron {intentos} intentos")
		break
	elif numero_es>numero:
		print("Es más grande")
	else:
		print("Es más pequeño")

	intentos==10
print("Perdiste :c")
print("El número de intentos es: ", intentos)