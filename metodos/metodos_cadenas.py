cadena1 = ""
cadena2 = ""

#convierte a mayusculas
masyusc = cadena1.upper()

#conierte a minusculas
minusc = cadena1.lower()

#primera letra en mayusculas
primera_letra_mayusc = cadena1.capitalize()

#bucamos una cadea en otra cadena, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coincidenza laza una excepción
busqueda_index = cadena1.index("D")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumérico devolvemos true, sino devlovmeos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadnea, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si no es asi devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si no es asi devuelve True
termina_con = cadena1.endswith("h")

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("la","lu")

#separa cadenas con la cadena que le pasamos
cadena_separada = cadena1.split(",")



print(es_alfanumerico)