"""Realizar un algoritmo para determinar cuánto ahorrará 
una persona en un año, si al final de cada mes deposita 
cantidades variables de dinero; además, se quiere saber 
cuánto lleva ahorrado cada mes."""

ahorroA=0

for mes in range(1,13):
	cantM=float(input(f"Cuanto has ahorrado en el mes {mes} ?:"))
	ahorroA+=cantM
	print("En el mes ", mes, " llevas ahorrado ", ahorroA)



