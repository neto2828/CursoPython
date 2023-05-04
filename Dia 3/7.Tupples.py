#Variable Tuple son inmutables
mi_tuple = (1,2,3,4)
print(type(mi_tuple))

#Consultar indice
print(mi_tuple[-2])

#anidar tuples
mi_tuple2 = (1,2,(10,20),4)
print(mi_tuple2[2])

#hacer castings
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

#asingar contenido a variables
t = (1,2,3,1)
x,y,z,w =t
print(x,y,z,w)

#pedir el lago
print(len(t))

#metodo Count contar
print(t.count(1))

#metodo Index consultar valor
print(t.index(1))