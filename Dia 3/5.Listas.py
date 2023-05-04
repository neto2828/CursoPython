#Lista Prueba
mi_lista = ['a', 'b', 'c']
otra_lista = ['hola',55,6.1]

#Impresión del tipo
print(type(mi_lista))
print(type(otra_lista))

#imprimir el numero de elementos de la lista
resultado = len(mi_lista)
print(resultado)

#indexar listas
resultado= mi_lista[0]
print(resultado)

#concatenar listas
resultado= mi_lista + otra_lista
print(resultado)

#modificar listas ya que estas son mutables
otra_lista[0] = 'alfa'
print(otra_lista)

#Metodo Agregar
otra_lista.append('g')
print(otra_lista)

#Metodo Eliminar
otra_lista.pop(0)
print(otra_lista)

#Metodo Ordenar
lista = ['g', 'b', 'm', 'c', 'a']
lista.sort()
print(lista)

#Metodo Reverse para voltear la lista
lista.reverse()
print(lista)

