"""Diseñar un algoritmo que nos diga el dinero que 
tenemos (en euros y céntimos) después de pedirnos cuantas 
monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 
céntimos)."""

monE2=int(input("Monedas de 2 euros: "))
monE1=int(input("Monedas de 1 euros: "))
monC50=int(input("Monedas de 50 centimos: "))
monC20=int(input("Monedas de 20 centimos: "))
monC10=int(input("Monedas de 10 centimos: "))

totalE=monE2*2+monE1
totalC=monC50*50+monC20*20+monC10*10
totalE=totalE+(totalC/100)
totalC=totalC%100

print(f"{totalE} euros y {totalC} céntimos")


