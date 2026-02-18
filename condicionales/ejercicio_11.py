"""Programa que lea 3 datos de entrada A, B y C. Estos 
corresponden a las  dimensiones de los lados de un 
triángulo.  El programa debe determinar que tipo de 
triángulo es, teniendo en cuenta: Si se cumple Pitágoras 
entonces es triángulo rectángulo Si sólo dos lados del 
triángulo son iguales entonces es isósceles. Si los 3 
lados son iguales entonces es equilátero. Si no se cumple
 inguna de las condiciones anteriores, es escaleno."""

ladoA=float(input("Introduce la longitud del lado A: "))
ladoB=float(input("Introduce la longitud del lado B: "))
ladoC=float(input("Introduce la longitud del lado C: "))

if (ladoA**2+ladoB**2==ladoC**2)or(ladoB**2+ladoC**2==ladoA**2)or(ladoC**2+ladoA**2==ladoB**2):
	print("Triángulo rectángulo")
if (ladoA==ladoB and ladoA!=ladoC)or(ladoB==ladoC and ladoB!=ladoA) or (ladoC==ladoA and ladoC!=ladoB) :
	print("Triángulo Isósceles")
else:
	if (ladoA==ladoB and ladoA==ladoC):
		print("Triángulo Equilátero")
	else:
		print("Triángulo Escaleno")






