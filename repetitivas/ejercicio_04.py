"""//Realizar un algoritmo que pida números <
(se pedirá por teclado la cantidad de 
//números a introducir). El programa debe 
informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0."""

contNeg=0
contPos=0
contCero=0

cantNum=int(input("¿Cuantos números vas a introducir? "))
for i in range(1, cantNum+1):
	numero=float(input("Número:"))
	if numero>0:
		contPos=contPos+1
	elif numero<0:
		contNeg=contNeg+1
	else:
		contCero=contCero+1

print("Números positivos: ", contPos)
print("Números negativos: ", contNeg)
print("Números igual a 0: ", contCero)
