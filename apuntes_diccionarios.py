# Diccionarios # 

# enga2val = {'one' : 'uno', 'step' : 'paso', 'book':'libro'}
# print (enga2val) 
# print(type(enga2val))
# print ('one es español es: {}'.format(enga2val['one']))

# print ('la longitud del diccionario es de: {}'.format(len(enga2val)))
# print ('esta la palabra house en el diccionario?: {}'.format('house' in enga2val['one']))ç

# enga2val['plane'] = 'avion'
# print(enga2val) 

# enga2val['ship'] = ['barco', 'enviar']  
# print(enga2val) 

# # ejercicio 
# cliente1 = {'nombre': 'Gustavo', 'apellidos' : 'Gomez', 'año_alta' : 2014, 'appMovil' : True} 
# cliente2 = {'nombre': 'Adrian', 'apellidos' : 'Gomez', 'año_alta' : 2017, 'appMovil' : False} 


# # Funcion que aplique descuento por año + 1% mas por la app
# # activada, me tiene que devolver la ficja actualizada

# def calculo_promo(cliente):
#     descuento = 0
#     if cliente['appMovil'] == 'True':
#         descuento += 1
#     descuento_antiguedad = cliente['año_alta']
#     descuento_antiguedad_apl = 2020 - descuento_antiguedad
#     descuento = descuento + descuento_antiguedad_apl
#     cliente['promo_antiguedad'] = descuento  
#     return cliente

# resultado = calculo_promo(cliente1)
# resultado2 = calculo_promo(cliente2)
# print('La ficha del nuevo cliente 1 es {}'.format(resultado))  
# print('La ficha del nuevo cliente 2 es {}'.format(resultado2))  


# Ejercicio:

# lector = {'id':324, 'nombre':'Miguel', 'prestados':set(['Tormenta de espadas'])}

# def prestado(lector, titulo):
#     libros = lector['prestados']
#     if titulo in libros:
#         return True
#     else:
#         return False

# ##resultado_presta = prestado(lector, 'Tormenta de espadas')
# ##print(resultado_presta)

# def presta (titulo, lector):
#     if prestado(lector, titulo):
#         print('El lector {} ya tiene prestado {}'.format(lector[id], titulo))
#         return lector
#     else:
#         lector['prestado'].add(titulo)
#         print('Se ha prestado {} al lector {}'.format(titulo, lector['id']))
#         return lector 

# resultado_presta =#...
# print() 

# Ejercicio: carrito: lsita de diccionarios

carrito = [
    {'desc':'Camara Reflex', 'cantidad':1, 'precio_unidad': 349.00
    },{
        'desc':'Bateria Canon', 'cantidad':1, 'precio_unidad': 24.87
    },{
        'desc':'Filtro Polarizador 35mm', 'cantidad':3, 'precio_unidad': 17.034
    }
]

# def total_compra(carro):
#     total = 0
#     for i in carro:
#         producto = i['cantidad']*i['precio_unidad'] 
#         total = total + producto
#     print('El valor de la compra es de {} '.format(total)) 
#     return total

# resultado = total_compra(carrito)


# Ejercicio, actualizar carro

# def esta_en_carro(carrito: list, producto: dict):
#     for i in carrito:
#         if i['desc'] == producto['desc']:
#             return True
#     return False

# resultado = esta_en_carro(carrito, 'Camara Reflex')
# print(resultado)

# def actualiza_carro(carrito: lista, producto: dicc):
#     if esta_en_carro(carrito, producto):
#         for elem in carrito:
#             if elem['desc'] == producto['desc']:  
#                 elem['cantidad'] = elem['cantidad'] + producto['cantidad'] 
#     else:
#         carrito.append(producto)
#     return carrito


#Ejercicio 

# clientes = [{'nombre': 'Gustavo', 'apellidos' : 'Gomez', 'año_alta' : 2014, 'appMovil' : True, 'promo_antiguedad': 7},
#  {'nombre': 'Luisa', 'apellidos' : 'Castaño', 'año_alta' : 2019, 'appMovil' : False, 'promo_antiguedad': 1}] 

# def elimina_promo(clientes):
#     for n in clientes:
#         promo = n.pop('promo_antiguedad')
#     return clientes

# resultado = elimina_promo(clientes)
# print(clientes)
