"""Crea un programa que pida al usuario dos número y muestre 
su división si el segundo no es cero, o un mensaje de aviso
en caso contrario"""

dividendo=int(input("Ingresa el primer numero: "))
divisor=int(input("Ingresa el segundo numero: "))

if divisor==0:
	print("No puedes dividir por 0")
else:
	print("La división es: ", dividendo/divisor)
