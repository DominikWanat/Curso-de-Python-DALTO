
#creando una lista (se puede modificar)
lista =["Dominik Wanat","no tengo", True, 1.80]

#creando una tupla (no se puede modificar)
tulpa = ("Lucas Dalto", "Soy Dalto", True, 1.80)

#esto es válido
lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"

#creando un conjunto (set) (no se accede a elementos por índice, no almacena datos duplicado)

conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) (la estrucutra es key : value y separamos por comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : "Soy Dalto"
}

print (lista[1])
