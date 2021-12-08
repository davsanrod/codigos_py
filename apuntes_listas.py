# a =[1,2, 34, 67,7]
# b =['hola', 'mundo'] 
# c =[1, 2 ,3 , 4, 'hola', 5.0]  

# entero = 34
# numflot = 45.5
# d=[entero, numflot]
# print('Las listas:  ',a, b) 
# print('La lista c: ', c)

# primer_elemento_a = a[0] 
# print('El primer elemento de la lista a es: ',primer_elemento_a)
# a[4] = 1000 #modifico el elemento 4 de a
# #print('Ultimo elemento de la lista a nuevo: 'a[4])  

# #Ultimo elemento 
# print("El ultimo elemento es {}".format(a[4]))

#Logitud de la lista 
# print("La lista mide: {}".format(len(a)))

# # # # # # # # 

clase = ['Operador de camara', 'Edu', 'David', 'Sara']

# rango = range(len(a)) 
# for indice in rango:
#     print ('Nombre de alumno: ', clase[indice])
#     #print ('El alumno {} ha venido a clase'.format(clase[indice]))
#     if clase[indice] == 'Sara':
#         print('La alumna {} no ha venido a clase'.format(clase[indice])) 
#     else:
#         print ('El alumno {} ha venido a clase'.format(clase[indice]))

# print('Es Sara parte de la clase?: {}'.format('Sara' in clase))

# matriz1 = ([1, 2, 3],  [1, 2, 3], [1, 2, 3])
# print(matriz1) 
# fila_que_no_se_si_esta = [1, 0, 0] 
# pertenece = fila_que_no_se_si_esta in matriz1
# print('Esta_es_la_fila 1,0,0 de la matriz?: {}'.format(pertenece))

# bbdd =['David', 'Edu', 'Sara'] 
# bbdd2 = ['David', 'Sara', 'Edu']
# print('Son iguales las listas? {}'.format(bbdd==bbdd2))


matriz2 =[ [1,2,3], [5,4], [6,7,8,9], [10] ]
# rango = range(len(matriz2))
# que_busco= int(input("Que quieres buscar?: "))
# for indice in rango:
#     #Dentro de una fila, voy mirando los elementos 
#     for indice_fila in range(len(matriz2[indice])):
#         if que_busco == matriz2[indice][indice_fila]: 
#             print('Si, está')
#             break
# else:
#     print('No está')

# for fila in matriz2:
#     print(fila)
#     if que_busco in fila:
#         print("está {}".format(que_busco))
        

carrito = [ ['camara reflex', 1, 349.99], 
            ['Tripode,', 2, 45.95], 
            ['Bateria NIKON', 3, 25.87] ]

# print(carrito)

# def total_compra(carro): 
#     n = 0
#     for i in carro:
#         añadido = i[1]*i[2]
#         n = n + añadido
#     print("El valor de la compra es de {}".format(n))
#     return n

# total_carrito = total_compra(carrito)
# ## print("El valor de la compra es de {}".format(total_carrito))


libro = ['en', 'un', 'lugar', 'de', 'la', 'mancha', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme']
# print ('mi libro tiene {} palabras'.format(len(libro))) 

#libro[5] #palabra de la posicion 5
#libro[5:9] #esto es una lista de la posicion 5 a la 9
#print([5:9])     
#                       #estas subslistas son excluyentes por la derecha, es decir, del elemento 5 al 8 incluido
#print[5:]    #imprimir del 5 al final
#print[:5]   #imprime desde el principio al 4, del 0 al 4, el 5 no lo coje, es exclusivo
#print('la primera mitad del libro es {} y la otra es {}').format(libro[:5], libro[5:]))      
#print(libro[1, -1])  #omite primero y ultimo
# print(libro[:])   #lo devuelve todo, es decir, devuelve una copia de la lista   
#print(libro[1:-1:2])  #cogeme los elementos omitiendo el primero y el ultimo pero de dos en dos




#Operaciones con una lista 
# libro[0] = libro[0].capitalize()  #primer elemento en minuscula    
# libro.append('vivia')  #añadir elemento, de forma secuencial
# libro.insert(2, 'AA')  #añadir elemento en la posicion 2
# libro.remove('AA') #eliminar elemento
# libro.pop('4')  #Va a la lista, te devuelve el elemento (es decir, lo puedo almacenar en una variable) y luego la borra
#                            #es decir, la extrae
#print('Lo que habia en el indice 4 es {}'.format(my_variable))
# print(libro.count('de')) #contar las apariciones del elemento
# libro.clear()  #deja vacia la lista 
# libro.index('de')   #indice donde aparece por primera vez un elemento
# print("Dada la vuelta la lista {}".format(libro.reverse()))
#              #devuelve 'none' porque?: porque solo actua, no muestra nada  
#              #si vuelves a imprimir ahora si lo muestra  
# print('Ordenado: {}'.format(libro.sort()))   #ordena, por numero, alfabeticamente  
#               #tb delvuelve none pero actua
#  Ojo: estas dos modifican la lista, si no quiero perderla debo actuar sobre un clon de la lista
# print('Ordenado: {}'.format(libro.sort(reverse = True)))   #ordena en orden inverso.




#Hacer programa donde añada a carrito de compra una lista 


# #carrito = [ ['camara reflex', 1, 349.99], 
#             ['Tripode,', 2, 45.95], 
#             ['Bateria NIKON', 3, 25.87] ]

descripcion = str(input('Introduzaca nombre del producto: '))
cantidad = int(input('Introduzaca la cantidad: '))
precio_unitario = float(input('Introduzaca el precio del producto: '))

def añadir(carrito, descripcion, cantidad, precio_unitario):
    lo_que_añado = [descripcion, cantidad, precio_unitario]
    carrito.append(lo_que_añado)
    return carrito

carrito_resultante = añadir([],descripcion, cantidad, precio_unitario)
print(carrito)
