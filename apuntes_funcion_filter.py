#Apuntes filter function 

def es_positivo(num):
    return num >= 0

lista = [-21,2, 4, -4, 5, -5, -8] 
mapa_resultado = filter(es_positivo, lista)
print(list(mapa_resultado))

#filter, para funciones que devuelves true o false en el caso de los true te devuelve los valores en una lista 

resultado = filter(lambda num: num >=0, lista)
print(list(resultado))

#Dado una lista de caracteres, nos filtre solo las vocales
lista_caracteres = ['a', 'b', 'r', 'k', 'u']
def es_vocal(car):
    vocales= ['a', 'e', 'i', 'o', 'u'] 
    if car in vocales:
        return True
    else:
        return False
resultado2 = filter(es_vocal, lista_caracteres)
print(list(resultado2))
resultado3 = map(es_vocal, lista_caracteres)
print(list(resultado3))