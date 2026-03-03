"""Escribe un programa que dados dos números, uno real 
(base) y un entero positivo (exponente), saque por pantalla 
el resultado de la potencia. No se puede utilizar el 
operador de potencia."""


base=float(input("Dame la base de la potencia: "))

while True:
	expo=int(input("Dame el exponente de la potencia: "))
	if expo<0:
		print("ERROR: El exponente debe ser positivo.")
	else:
		break

potencia=1
for i in range(1, expo+1):
	potencia=potencia*base

print("Potencia ", potencia)			
