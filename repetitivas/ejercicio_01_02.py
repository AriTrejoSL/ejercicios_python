print("Programa que calcula el factorial de un número")

nume= int(input("Ingresa un número: "))
factorial=1
for i in range(1, nume+1):
	factorial=factorial*i
print("El factorial es: ",factorial)
