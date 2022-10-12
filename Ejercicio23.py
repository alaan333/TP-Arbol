# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.
 
from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_criaturas,
    agregar_dato,
    busqueda,
    agregar_descripcion_a_todos,
    tres_mayores,
    criaturas_derrotadas_heracles,
    criaturas_capturadas_heracles,
    criaturas_no_derrotadas,
    agregar_capturador,
    inorden_empieza_con,
    eliminar_nodo,
    modificar_info,
    inorden,
    crear_bosque,
    contar_nodos,
    por_nivel
)

class Datos_de_criaturas:
    def __init__(self,derrotadaPor,datosExtras,atrapadaPor):
        self.derrotadaPor=derrotadaPor
        self.datosExtras=datosExtras
        self.atrapadaPor=atrapadaPor

arbol_mitologia=nodoArbol()
file=open('C:/Users/Fernando Paz/Primer proyecto JS/Algoritmo2022/Algoritmo y estructura de datos/PythonAlan/Archivoslocales/Trabajo-practico-arbol/Mitologia.txt',encoding="utf8")
lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    dato = linea.split(';')
    dato[1] = dato[1][:-1]
    insertar_nodo(arbol_mitologia,dato[0],Datos_de_criaturas(dato[1],None,None))

# a. listado inorden de las criaturas y quienes la derrotaron;
inorden_criaturas(arbol_mitologia)
print()
# # b. se debe permitir cargar una breve descripción sobre cada criatura;
# -------------------------------Metodo especifico---------------------------------
buscado=input('Ingrese la criatura que desea agregar un dato: ').capitalize()
agregar_dato(arbol_mitologia,buscado)
#--------------------------------Metodo para todo el arbol-----------------------------------
# agregar_descripcion_a_todos(arbol_mitologia)

# c. mostrar toda la información de la criatura Talos;
criatura=busqueda(arbol_mitologia,'Talos')
if criatura:
    print(criatura['info'])
    print('Derrotado por: ',criatura['datos'].derrotadaPor)
    if (criatura['datos'].datosExtras!=None):
        print('Descripcion: ',criatura['datos'].datosExtra)
    else:
        print('No hay datos adicionales de Talos')
else:
    print('Esa criatura no está disponible')
print()

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

# e. listar las criaturas derrotadas por Heracles;
print('Criaturas derrotadas por heracles: ')
print(criaturas_derrotadas_heracles(arbol_mitologia))
print()

# # # f. listar las criaturas que no han sido derrotadas;
print('Criaturas no derrotadas: ')
criaturas_no_derrotadas(arbol_mitologia)
print()

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
vector=['Cerbero', 'Toro de Creta','Cierva Cerinea', 'Jabalí de Erimanto']
for v in vector:
    agregar_capturador(arbol_mitologia,v)

# i. se debe permitir búsquedas por coincidencia;
buscado=str(input('Ingrese lo que desea buscar: ')).capitalize()
inorden_empieza_con(arbol_mitologia,buscado)

# j. eliminar al Basilisco y a las Sirenas;
v_elim=['Basilisco','Sirenas']
for v in v_elim:
    eliminar_nodo(arbol_mitologia,v)
    print(f'Nodo de {v} eliminado')
print()

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
agregar_dato(arbol_mitologia,'Aves del Estínfalo')
print()

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
modificar_info(arbol_mitologia,'Ladón')

# m. realizar un listado por nivel del árbol;
print('Arbol por nivel: ')
por_nivel(arbol_mitologia)
print()

# n. muestre las criaturas capturadas por Heracles.
print('Criaturas capturadas por Heracles')
criaturas_capturadas_heracles(arbol_mitologia)