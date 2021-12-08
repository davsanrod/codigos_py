#Apuntes map

numero = [1,2,3,4,5,6,7,8,9,10]
cuadrados = []  

for n in (numero):
    cuadrado = n ** 2
    cuadrados.append(cuadrado)
print (cuadrados)

def elevar_cuadrado(numero):
    return numero ** 2
resultado_elevar = elevar_cuadrado(4)
print(resultado_elevar)

cuadrados_funcion= [] 
for i in numero:
    cuadrado= cuadrados_funcion.append(elevar_cuadrado(i))
print (cuadrados)


mapa_resultado = map(elevar_cuadrado, numero)
print(mapa_resultado)
#Nos devuelve un mapa, que no son legibles, los tenemos que pasar a lista
lista_resultado = list(mapa_resultado)
print(lista_resultado) 


print('\n\n\n\n\n\n')
#Crear una funcion que nos devuelva los caracteres en mayuscula

caracteres = ['a', 'b', 'c', 'd']
def mayusculas(caracter):
    return caracter.upper() 
mapa_caracteres= map(mayusculas, caracteres)
lista_caracteres = list(mapa_caracteres)
print(lista_caracteres)
# mas rapido:
# print(list(map(mayusculas, caracteres))) 


#Map con dos variables
def multiplicar(num1, num2):
    return num1 * num2

lista1 = [1, 23, 4, 56, 6]
lista2 = [33,44,55,66,7]
#las listas deben tener el mismo tamaño  
mapa_multiplicar = map(multiplicar, lista1, lista2)
print(list(mapa_multiplicar))



listaA = [4, 8, 10]
listaB = [2, 2, 3] 

def divisible(num1, num2):
    #return num1 % num2 == 0 
    if (num1 % num2 == 0):
        return True
    else:
        return False
mapa_divisible= map(divisible, listaA, listaB)
print(list(mapa_divisible))