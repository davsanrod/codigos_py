#Clase 24/09/20

#Repaso de ficheros clase anterior:
#Ejercicio, sacar los usuarios (fila 1) del archivo passwd 
manejador = open('/etc/passwd')
contenido_passwd = manejador.readlines()
for linea in contenido_passwd:
    print(linea.strip())

for linea in contenido_passwd:
    linea_limpia = linea.split(':')
    print(linea_limpia[0]) 


# Tuplas #  
lista = [1, 2, 3] 
tupla = (1, 2, 3)
#tupla[1] = 47      , esto da error

tupla2 = (1, 2, ('a', 4), 5) 
print(tupla2[2][0])

tupla_from_list= tuple(lista)
print(tupla_from_list)

for elemento in tupla_from_list:
    print(elemento)


#Asignacion multiple
print('\n\n')
x,y,z = tupla
print(x)
print(y)
print(z)


#Metodos de las tuplas
print('\n\n')
print('Conteo de tuplas')
tupla_count = (1,1,1,3,4,5,6,1,7) 
print(tupla_count.count(1)) #Cuenta las veces que aprece 1 en la tupla tupla_count 

print('Localizar elemento 3')
print(tupla_count.index(3))    #En que posicion esta el elemento 5 

#queremos saber todos los indices donde esten el elemento 1
#adaptacion del metodo index a mano
# contador = 0
# for elemento in tupla_count:
#     if elemento == 1:
#         print(tupla_count.index(1)) 
#     contador += 1


# print('\n \n') 
# print('Ejercicio busqueda de numero:')
# #Funcion donde usuario indica un numero de la tupla y nos dice cuantas veces esta repetido
# #para tupla_count

# indice_num_tupla = int(input('Introduce un numero para buscar: '))
# print(tupla_count.count(indice_num_tupla))


print('\n \n\n \n') 

# Named tuples # 
persona1 = {'nombre:': 'Carlos', 'edad': 29} 
persona2 = {'nombre:': 'Ana', 'edad': 23} 
persona3 = {'nombre:': 'Jose', 'edad': 24, 'pais': 'Spain'}

from collections import namedtuple
Persona = namedtuple ('Persona', ['nombre','edad'])
carlos = Persona (nombre= 'Carlos', edad= 29)
#jose_ = Persona (nombre= 'Jose', edad= 24, pais='Spain')



#Creamos named_tuple de 'factura', como la clase anterior
Factura = namedtuple ('producto', ['nombre','pvp','unidades','nvendidos'] ) 
producto_lejia = Factura(nombre= 'lejia', pvp= '1.25', unidades= 15, nvendidos=32)
print(producto_lejia)

#lejia ya es inmutable pero si podemos crear un metodo para crear uno nuevo con otro nombre a partir del anterior 
def cambia_nombre_producto(producto, nuevo_nombre):
    productoNuevo = Factura (nombre= nuevo_nombre,
                            pvp= producto.pvp,
                            unidades= producto.unidades,
                            nvendidos= producto.unidades
                            )
    return productoNuevo

nuevoProducto = cambia_nombre_producto (producto_lejia, 'neutrex')
print(nuevoProducto)




#Calcular la distancia entre dos puntos:
from math import sqrt          #sqrt es la raiz cuadrada 
pt1= (1.0, 5.0)
pt2= (2.5, 1.5)
distancia = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(distancia)

#Lo hacemos para una namedtuple
#       asi podemos evitar errorres futuros si repasamos
#       y ya no recuerdas a que se refiere la formulacion

Puntos = namedtuple ('Distancia', ['x', 'y'])
punto1= Puntos(x=1.0, y=5.0)
punto2= Puntos(x=2.5, y=1.5)
distancia2 = sqrt ((punto1.x - punto2.x)**2 +
                     (punto1.y - punto2.y)**2)
print(distancia2)



print('\n\n\n\n\n\n\n')
#Ejercicio, calcular la probabilidad de coincidir cumpleaños en una sala por numero de personas
from random import randrange

#Funcion que genere una lista aleatoria de n numeros entre 1 y 365 
def generar_cumpleanyos(n_generador):
    lista_aleatorios = []
    for contador in range(n_generador):
        n_generado = randrange(1, 365)
        lista_aleatorios.append(n_generado)
    return lista_aleatorios

#Funcion que compruebe si hay repetidos y devuelva true o false 
def repetidos(lista):
    lista_comprobar = len(lista)
    lista_conjunto = len(set(lista))
    if lista_comprobar == lista_conjunto:
        return False
    else:
        return True
       #Otro forma:
       # def repetidos(lista):
       #    return len(lista) = len(set(lista)) 

#Funcion que genere un grupo de n personas y devuelva true o false si hay repetidos
def generar_personas(n_personas):
    lista_personas = generar_cumpleanyos(n_personas)
    hay_repetidos = repetidos(lista_personas)
    return hay_repetidos

#Funcion que ejecute m pruebas sobre un grupo de n personas y devuelva el %
def estadisticas_grupo(m, n):
    contador = 0
    for i in range(m):
        if (generar_personas(n) == True):
            contador += 1
    porcentaje = contador / m *100
    return porcentaje
# resulado= estadisticas_grupo(25,15)
# print(resulado)

#Funcion que ejecute m pruebas con grupos de entre n1 y n2 personas
def estadisticas (m, n1, n2):
    lista_porcentajes = []
    for n in range(n1, n2+1):
        porcentaje = estadisticas_grupo(m,n)
        lista_porcentajes.append(porcentaje)
    return lista_porcentajes
resultado= estadisticas(10, 1, 25)
print(resultado)