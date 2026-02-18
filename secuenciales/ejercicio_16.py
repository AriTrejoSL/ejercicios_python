"""//Dos vehículos viajan a diferentes velocidades 
(v1 y v2) y están distanciados por una distancia d. 
El que está detrás viaja a una velocidad mayor. Se 
pide hacer un algoritmo para ingresar la distancia entre 
los dos vehículos (km) y sus respectivas velocidades (km/h)
y con esto determinar y mostrar en que tiempo (minutos) 
alcanzará el vehículo más rápido al otro."""

vel1=int(input("Ingresa la velocidad del primer coche: "))
vel2=int(input("Ingresa la velocidad del segundo coche: "))
D=int(input("Cual es la distancia entre los coches: "))

tiempo=D/(vel1-vel2)
tiempo=tiempo*60
print(f"Lo alcanza en {tiempo} minutos")