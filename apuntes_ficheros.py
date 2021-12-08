# #Apuntes ficheros

# manejador = open('/ruta/fichero')
# print(manejador)

# contenido_fichero = list(manejador)
# print('---CONTENIDO FICHERO---')
# print(contenido_fichero)

# print('---CONTENIDO FICHERO BIEN HECHO---')
# for linea in contenido_fichero:
#     print(linea)


# print('---CONTEO FICHERO---')
# #Lo mas facil seria con el metodo '.len()'
# # lo hacemos con el metodo contador para repasar
# contador = o
# for i in contenido_fichero:
#     contador += 1
# print(contador)


# print('---LIMPIAR CONTENIDO FICHERO---')
# for linea in contenido_fichero:
#     print(linea.strip)

# for linea in contenido_fichero:    #Otro metodo, menos aconsejado 
#     print(linea, end= '')


# print('---LEER FICHERO RL---')
# manejador = open('/ruta/fichero')
# contenido_fichero_RL = manejador.readlines() 
# print(contenido_fichero_RL)

# contenido_fichero_RLs = manejador.readline() 
# print(contenido_fichero_RLs)   #Este lee solo una linea
#                                #Para un csv interesa para leer solo la cabezera

# print('---LEER FICHERO withOpen---')
# with (open('/etc/hosts')) as hosts:
#     for linea in hosts:
#         print(hosts)


# # Ejercicio 
# manejador = open('/etc/hosts')
# lista_nueva = []   #Lista vacia, otro metodo =list()  
# with (open('/etc/hosts')) as hosts:
#     for host in hosts:
#         linea_limpea = host.strip()
#         #lista_nueva.append(lista_nueva) , este seria el metodo recomendado
#         lista_nueva = lista_nueva + [linea_limpea] 
#     print(lista_nueva)


# #otra forma de hacerlo 
# manejador = open('/etc/hosts')
# contenido_fichero = list(manejador)
# lista = [] 
# for linea in contenido_fichero:
#     if (linea.strip().startswith('#') == False ):
#         if ((linea.strip() != '')) :
#             lista = lista + [linea.strip()] 
# print(lista)



# #Division con split
# print('\n____DIVISION_SPLIT__\n') 
# manejador = open('/etc/hosts')
# contenido_fichero = list(manejador)
# lista = [] 
# for linea in contenido_fichero:
#     if (linea.strip().startswith('#') == False ) and (linea.strip() != ''):
#         lista.append(linea.strip(' ', maxsplit=1))
# print(lista)


# #Lectura fichero creado
# print('\n___Lectura fichero manual___\n') 
# manejador = open('/home/KSDESKTOP/icemd411/fichero')
# contenido_fichero = list(manejador)
# for linea in contenido_fichero:
#     print(linea)



# #Lectura fichero facturas
# print('\n___Lectura fichero facturas___\n') 
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# for linea in contenido_fichero:
#     print(linea.strip())



# print('\n____PARSEAR_PRODUCTO_FICHEROS__\n') 
# def parsear_producto(linea_producto):
#     salida = linea_producto.split().split(',')
#     return salida 
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# for linea in contenido_fichero:
#     print(parsear_producto(linea))



# print('\n____PARSEAR_PRODUCTO_FICHEROS_CON_NOMBRE__\n') 
# def producto_listado(linea_producto):
#     #producto = parsear_producto(linea_producto)
#     producto = linea_producto.splip().split(',')
#     return{ 
#         'nombre_producto': producto[0],
#         'cantidad': producto[1],
#         'pvp': producto[2],
#         'vendidos': producto[3]
#     } 
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# for linea in contenido_fichero:
#     print(parsear_producto(linea))




#Escritura ficheros 
# manejador = open('/home/KSDESKTOP/icemd411/fichero_nuevo', 'w')
# manejador.write('Hola amigos \n')
# manejador.close()

# manejador = open('/home/KSDESKTOP/icemd411/fichero_nuevo', 'a')
# manejador.write('Adios amigos \n')
# manejador.close()

# manejador = open('/home/KSDESKTOP/icemd411/fichero_nuevo', 'w')
# manejador.write('Hola amigos \n')
# manejador.write('Adios amigos \n')
# manejador.close()


# #Copiar fichero factura en uno nuevo, factura2 
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# #Manejador para escribir 
# manejador_escritura = open('/home/KSDESKTOP/icemd411/Documentos/factura2','w')
# for linea in contenido_fichero:
#     manejador_escritura.write(linea)


# #Añadir al fichero 
# manejador_escritura = open('/home/KSDESKTOP/icemd411/Documentos/factura2','a')
# manejador_escritura.write('tomate,10,1.50,50\n')
# manejador_escritura.close()


# #Escritura fichero (copia) con el metodo writelines 
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# manejador_escritura = open('/home/KSDESKTOP/icemd411/Documentos/factura2','w')
# manejador_escritura.writelines(contenido_fichero)


# #Metodo escritura print 
# manejador_escritura = open('/home/KSDESKTOP/icemd411/Documentos/factura2','w')
# print('Otro metodo que solo usaria tratamientos raros a str! no se recomienda', file = manejador_escritura)
# manejador_escritura.close()


# #Escritura metodo with_open
# with(open('/home/KSDESKTOP/icemd411/Documentos/factura2', 'w')) as ficherosalida:
#     ficherosalida.write('hola mundo\n') 



#Ejercicio: separar ficheros
# manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
# contenido_fichero = manejador.readlines()
# for linea in contenido_fichero:
#     print(linea.strip())

# manejador_par = open('/home/KSDESKTOP/icemd411/Documentos/factura_par', 'w')
# manejador_inpar = open('/home/KSDESKTOP/icemd411/Documentos/factura_inpar', 'w')
# contador = 0
# for linea in contenido_fichero:
#     if linea %2 == 0:
#         manejador_par.write(linea)
#     contador += 1
#     else:
#         manejador_inpar.write(linea)

#solucion 
# with(open('directorio','w')) as pares:
#   contador = 0
#   for linea in contenido_factura:
#       if (contador %2 == 0):
#           pares.write(linea)
#       contador += 1
# 
# 
# solucion 2
# contenido_factura = list(open(directorio))
# with(open(directorio)) as pares:
#   pares.writelines(contenudo[::2])
# with(open(directorio)) as impar:
#   impar.writelines(contenido[1::2]) 

#segundo intento ejercico 
manejador = open('/home/KSDESKTOP/icemd411/Documentos/factura')
contenido_fichero = manejador.readlines()
for linea in contenido_fichero:
    print(linea.strip())

contenido_factura = list(open(/home/KSDESKTOP/icemd411/Documentos/factura))
with(open(/home/KSDESKTOP/icemd411/Documentos/factura)) as pares:
  pares.writelines(contenudo[::2])
with(open(/home/KSDESKTOP/icemd411/Documentos/factura)) as impar:
  impar.writelines(contenido[1::2])