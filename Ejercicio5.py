# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    contar_nodos
)

arbol = nodoArbol()
arbol_villanos=nodoArbol()
arbol_heroes=nodoArbol()


lista = [
    ['iron man', False],
    ['capiana marvel', False],
    ['thor', False],
    ['dotor strange', False],
    ['thanos', True],
    ['red skull', True],
    ['capitan america', False],
]

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
for nombre, villano in lista:
    insertar_nodo(arbol, nombre, villano)

# b. listar los villanos ordenados alfabéticamente;
print('Villanos en el arbol: ')
inorden_villano(arbol)
print()

# c. mostrar todos los superhéroes que empiezan con C;
print('Superheroes que empiezan con C: ')
inorden_empieza_con(arbol, 'c')
print()

# d. determinar cuántos superhéroes hay el árbol;
print('Cantidad de superheroes en el arbol: ')
print(contar_heroes(arbol))

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
clave = input('ingrese parte de lo que desea buscar ')
inorden_empieza_con(arbol, clave)
print()
clave = input('ingrese nombre que desea modificar ')
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input('ingrese nuevo nombre ')
    insertar_nodo(arbol, name, False)
else:
    print('valor no encontrado en el arbol')

# f. listar los superhéroes ordenados de manera descendente;
print()
print('Lista heroes desendente del arbol')
postorden_heroes(arbol)
print()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

crear_bosque(arbol,arbol_heroes,arbol_villanos)
print(f'Cantidad de nodos del arbol heroes: {contar_nodos(arbol_heroes)}')
print(f'Cantidad de nodos del arbol villanos: {contar_nodos(arbol_villanos)}')
print()
print('Arbol de heroes:')
inorden(arbol_heroes)
print()
print('Arbol de villanos:')
inorden(arbol_villanos)
print()