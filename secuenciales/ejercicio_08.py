#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
#en cuenta su sueldo base y comisiones.

sueldob=int(input("Ingresa tu sueldo base: "))
venta1=int(input("Ingresa tu primera venta: "))
venta2=int(input("Ingresa tu segunda venta: "))
venta3=int(input("Ingresa tu tercera venta: "))

ventasf=venta1+venta2+venta3
comision=(ventasf)*.10
sueldof=sueldob+comision

print(f"Tu sueldo base es de ${sueldob}, el total de tu comision es de ${comision}, tu sueldo final es de ${sueldof}")