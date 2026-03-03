"""//Algoritmo que muestre la tabla de 
multiplicar de los números 1,2,3,4 y 5."""

print("Tabla de mutiplicar del 1 al 5")

for tabla in range(1,6):
	for num in range(1,11):
		print(tabla, " * ", num, " = ", tabla*num)
	input("Pulsa una tecla para poder continuar")
