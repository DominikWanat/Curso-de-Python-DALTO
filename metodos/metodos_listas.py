
#creando una lista con list()
lista = list([20, 0 , -1, 24, 1])

#devuelve la cantidad de elementos ade la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
#lista.append("JAJAJAJA")

#agregando un elemento a la lista en un índice específcio
#lista.insert(2,"insertando")

#agregando varios elementos a la lista
lista.extend([False,2030, True])

#eliminado un elemento de la lista (por índice)
lista.pop(0) #si utilizamos elementos negativos -1 eliminamos el último

#rmoviendo un elemento de la lista por su valor
#lista.remove("insertando")

# ordena los elementos de la lista
lista.sort()             #ordena de menor a mayor False, True, numeros
lista.sort(reverse=True) #ordena de mayor a menor numeros, True, False

#invierte los elementos de una lista
lista.reverse()


#eliminado todos los elementos de la lista
#lista.clear()
print(lista)

#nos enseña que pnodemos hacer con el elemento
print(dir("lista"))


