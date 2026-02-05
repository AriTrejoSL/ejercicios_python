"""Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los 
radios r1,r2 de dos 
//circunferencias y las clasifique en uno de estos estados:
//exteriores
//tangentes exteriores
//secantes
//tangentes interiores
//interiores
//concéntricas"""

cordenadaX1=float(input("Dame la coordenada x para la primer circunferencia: "))
cordenadaX2=float(input("Dame la coordenada x para la segunda circunferencia: "))
radio1=float(input("Dame el radio de la primer circunferencia: "))

cordenadaY1=float(input("Dame la coordenada y para la primer circunferencia: "))
cordenadaY2=float(input("Dame la coordenada y para la segunda circunferencia: "))
radio2=float(input("Dame el radio de la segunda circunferencia: "))

distancia=(((cordenadaX2-cordenadaX1)**2)+((cordenadaY2-cordenadaY1)**2))**0.5

if distancia>(radio1+radio2):
	print("Circunferencias exteriores")
if distancia==(radio1+radio2):
	print("Circunferencias tangentes exteriores")
if distancia<(radio1+radio2):
	print("Circunferencias secantes")
if distancia==abs(radio1-radio2):
	print("Circunferencias tangentes interiores")
if distancia>0 and distancia<abs(radio1-radio2):
	print("Circunferencias interiores")
if distancia==0:
	print("Circunferencias concéntricas")
