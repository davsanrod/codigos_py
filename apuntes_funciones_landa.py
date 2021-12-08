# Funciones Lambda

def doblar_num (num) :
    num = num *2
    return num

# def doblar_num2 (num):
#     return num = num*2

lambda num: num*2
doblar = lambda num: num*2
print(doblar(20))
#Otra manera de imprimir funciones


#Crear funciones lambda que devuelva par o impar
num_par = lambda num: num % 2 == True
print(num_par(5)) 

#Funcion suma 
sum = lambda x, y: x + y
print(sum(10, 5))


#Crear funcion lambda (con map) para elevar todos los numeros de una lista al cuadrado 
lista = [1, 5,6,19, 23]
mapa_resuelto = map(lambda num: num ** 2, lista)
print(list(mapa_resuelto))