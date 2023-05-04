#Variable Set
mi_set= set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2,3}
print(type(otro_set))
print(otro_set)

#metodo lend
print(len(otro_set))

#consultas
print(2 in mi_set)

#union de Set
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#metodo add
s1.add(4)
print(s1)

#metodo eliminar
s1.remove(3)
print(s1)

#metodo descartar
s1.discard(4)
print(s1)

#pop, elimina un elemento aleatorio
s1.pop()
print(s1)

#metodo clear
s1.clear()
print(s1)