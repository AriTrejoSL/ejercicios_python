"""Una compañía de transporte internacional tiene servicio en algunos países de 
// América del Norte, América Central, América del Sur, Europa y Asia.
// El costo por el servicio de transporte se basa en el peso del paquete 
// y la zona a la que va dirigido..."""

peso=int(input("¿Que peso tiene el paquete (gramos)? "))
if peso>0 and peso<=500:
	print("1. América del Norte")
	print("2. América Central")
	print("3. América del Sur")
	print("4. Europa")
	print("5. Asia")
	zona=int(input("¿A que zona se reparte (1 a 5)? "))
	if zona==1:
		print("El coste es de ", peso*24, "euros")
	elif zona==2:
		print("El coste es de ", peso*20, "euros")
	elif zona==3:
		print("El coste es de ", peso*21, "euros")
	elif zona==4:
		print("El coste es de ", peso*10, "euros")
	elif zona==5:
		print("El coste es de ", peso*18, "euros")
	else:
		print("Zona incorrecta")
else:
	print("Peso incorrecto (no podemos transportar paquetes de más de 5 kg)")

