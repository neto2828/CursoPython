#Variable de diccionario
diccionario = {'nombre':'Juan','paterno':'Fuentes','Peso':15, 'Talla':1.76}

#typo de elemento
print(type(diccionario))
print(diccionario)

#obtener el valor de un elemento del diccionario
consulta = (diccionario['paterno'])
print(consulta)

#Diccionario mas complejo
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

#ejercicio imprimir la letra e en mayuscula con 1 sola linea
dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())

#agregar elemenos a un diccionario
dic3 = {1:'a',2:'b'}
print(dic3)
dic3[3] = 'c'
print(dic3)

#sobrescribir elemento del diccionario
dic3[2] = 'B'
print(dic3)

#imprimir claves de diccionario
print(dic3.keys())
#imprimir valores de diccionario
print(dic3.values())
#imprimir diccionario
print(dic3.items())