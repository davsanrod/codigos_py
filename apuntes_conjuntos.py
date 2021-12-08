# Apuntes conjuntos #

# lista = []
# lista = list[] 
# conjuntos = {}  
# conjuntos = set{[]}  #Crear un conjunto a partir de una lista 

# conjuntos = {1, 2, 3, 4, 5} 
# print('Esra 10 en el conjunto?'.format(10 in conjunto))

# Cosas que puedo hacer con un conjunto, el anterior es para ver si esta, el resto de funciones estan en ,os apuntes del profesor bien escrito
# format(len(conjunto)) saber si tiene
#
# conjunto.add() añadir
# conjunto.remove() eliminar
# 
# conjunto.pop() extrae un elemento al azar

# Vamos a definir una funcion que recibe dos conjuntos y nos devuelve los elementos comunes 

# def interseccion(conj1, conj2):
#     conjunto_interseccion = set{} 
#     for elemento in conj1:
#         if elemento in conj2:
#             conjunto_interseccion.add(elemento)
#     return conjunto_interseccion

# Funcion que nos diga si un conjunto es subconjunto de otro#

# con1= {1, 2, 3, 4}
# con2= {1, 2}

# def es_subconjunto(set1, set2):
#     sub_con = set()
#     for elemento in set1:
#         if elemento in set2:
#             sub_con.add(elemento)
#     if set2 == sub_con:
#         return True
#     else:
#         return False

# resultado1 = es_subconjunto(con1, con2)
# print('Es subconjunto con2 de con1?: {} '.format(resultado1))


# Funcion simetrica que dvuelve ,a diferencia # 

# conjuntoA = {1, 2, 3, 4, 5}
# conjuntoB = {4, 5, 6, 7, 8, 9}

# def diferencia_simetrica(set1, set2):
#     conjunto_dif = set()
#     for elemento in set1:
#         if elemento not in set2:
#             conjunto_dif.add(elemento)
#     for elemento in set2:
#         if elemento not in set1:
#             conjunto_dif.add(elemento)
#     return conjunto_dif

# resultado_dif = diferencia_simetrica(conjuntoA, conjuntoB)
# print('El conjunto de diferencia simetrica es: {} '.format(resultado_dif))
