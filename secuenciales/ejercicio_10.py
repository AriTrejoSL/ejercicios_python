"""Un alumno desea saber cual sera su calificacion final de la materia 
de algoritmos. Dicha calificacion se compone de los siguientes porcentajes:
55% del promedio de sus 3 calificacion del examenes parciales
30% de la calificacion de su examen final
15% de la calificacion de un trabajo final"""

print("Calificaciones parciales")
cal1=float(input("Ingresa tu primera calificación: "))
cal2=float(input("Ingresa tu segunda calificación: "))
cal3=float(input("Ingresa tu tercera calificación: "))

PromC=(cal1+cal2+cal3)/3

calEF=float(input("Ingresa la calificacion de tu examen final: "))
calTF=float(input("Ingresa la calificacion de tu trabajo final: "))

CF=(PromC*0.55)+(calEF*0.3)+(calTF*0.15)

print("Tu calificacion final es de ", CF)