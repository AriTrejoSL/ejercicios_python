"""Un ciclista parte de una ciudad A a las HH horas, 
MM minutos y SS segundos. El tiempo de viaje hasta llegar 
a otra ciudad B es de T segundos. Escribir un algoritmo 
que determine la hora de llegada a la ciudad B."""

import math

hs=int(input("Hora de salida: "))
ms=int(input("Minutos de salida: "))
ss=int(input("Segundos de salida: "))
tsl=int(input("Tiempo en segundos que tardaste en llegar: "))

si=hs*3600+ms*60+ss
sf=si+tsl

hll=math.trunc(sf/3600)
mll=math.trunc((sf%3600)/60)
sll=math.trunc(sf%3600)%60

print("Hora de llegada")
print(f"{hll} horas {mll} minutos {sll} segundos")
