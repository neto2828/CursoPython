#Situcción: se trabaja en una empresa donde los vendedores reciben una comisión del 13% por la venta total
#Crear un programa donde se pregunte su nombre y el total vendido en el mes
#el programa debe mostrar su nombre y el total de comisiones


nombre = input(("Cual es tu nombre: "))
ventas = input(("Total vendido en el mes: "))

comision = round(((float(ventas) * 13)/100),2)

print(f"Ok, {nombre} tus ventas obtenidas son ${ventas} y tu comisión del 13% es de ${comision}")