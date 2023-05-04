#Crear un analizador de texto
#Crear un programa que se solcite ingresar un texto
#luego solicitar que el usuario ingrese 3 letras a su eleccion
#el programa devolvera lo siguiente
#   1 cuantas veces aparece cada letra (usar lista)
#   2 cuantas palabras hay en todo el texto
#   3 primer letra del texto y de la ultima (index)
#   4 invertir el orden de las palabras
#   5 buscar la palabra "python" dentro del texto (diccionario)

mi_lista = []
texto = input("Ingresa tu texto")
texto = texto.lower()

mi_lista.append(input("ingresa la 1 letra a buscar").lower())
mi_lista.append(input("ingresa la 2 letra a buscar").lower())
mi_lista.append(input("ingresa la 3 letra a buscar").lower())
mi_lista.append(input("ingresa la 4 letra a buscar").lower())
mi_lista.append(input("ingresa la 5 letra a buscar").lower())

total1 = texto.count(mi_lista[0])
total2 = texto.count(mi_lista[1])
total3 = texto.count(mi_lista[2])
total4 = texto.count(mi_lista[3])
total5 = texto.count(mi_lista[4])

print("Mi texto es: " + texto)
print(f"Tiene  '{mi_lista[0]}' repetida {total1} veces")
print(f"Tiene  '{mi_lista[1]}' repetida {total2} veces")
print(f"Tiene  '{mi_lista[2]}' repetida {total3} veces")
print(f"Tiene  '{mi_lista[3]}' repetida {total4} veces")
print(f"Tiene  '{mi_lista[4]}' repetida {total5} veces")

palabras = texto.split()
print(f"En el texto hay {len(palabras)} palabras")

letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial del texto es '{letra_inicio}' y la final es '{letra_final}'")

mi_lista.reverse()
print(f"El orden inverso de las palabras es '{mi_lista}'")

buscar_python = 'python' in texto
dic= {True: "Si", False:"No"}

print(f"La palabra phyton existe en el texto? {dic[buscar_python]}")









