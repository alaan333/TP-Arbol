from string import octdigits
from cola import Cola


def nodoArbol():
    nodo = {
        'info': None,
        'datos': None,
        'der': None,
        'izq': None,
        'altura': 0,
    }
    return nodo


def copiar_nodo(nodo_datos, nodo_copia):
    if nodo_datos:
        nodo_copia['info'] = nodo_datos['info']
        nodo_copia['der'] = nodo_datos['der']
        nodo_copia['izq'] = nodo_datos['izq']
        if 'datos' in nodo_copia:
            nodo_copia['datos'] = nodo_datos['datos']


def insertar_nodo(arbol, dato, datos=None):
    if arbol['info'] is None:
        arbol['info'] = dato
        arbol['datos'] = datos
    elif dato < arbol['info']:
        if arbol['izq'] is None:
            arbol['izq'] = nodoArbol()
        insertar_nodo(arbol['izq'], dato, datos)
    else:
        if arbol['der'] is None:
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato, datos)
    balancear(arbol)
    actualizar_altura(arbol)


def altura(arbol):
    if arbol is None:
        return -1
    else:
        return arbol['altura']


def actualizar_altura(arbol):
    if arbol is not None:
        alt_izq = altura(arbol['izq'])
        alt_der = altura(arbol['der'])
        arbol['altura'] = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(arbol, control):
    aux = nodoArbol()
    if control:
        copiar_nodo(arbol['izq'], aux)
        arbol['izq'] = None
        if(aux['der'] and not arbol['izq']):
            arbol['izq'] = nodoArbol()
        copiar_nodo(aux['der'], arbol['izq'])
        aux['der'] = nodoArbol()
        copiar_nodo(arbol, aux['der'])
    else:
        copiar_nodo(arbol['der'], aux)
        arbol['der'] = None
        if(aux['izq'] and not arbol['der']):
            arbol['der'] = nodoArbol()
        copiar_nodo(aux['izq'], arbol['der'])
        aux['izq'] = nodoArbol()
        copiar_nodo(arbol, aux['izq'])
    arbol.update(aux)
    actualizar_altura(aux['izq'])
    actualizar_altura(aux['der'])
    actualizar_altura(aux)


def rotar_doble(arbol, control):
    if control:
        rotar_simple(arbol['izq'], False)
        rotar_simple(arbol, True)
    else:
        rotar_simple(arbol['der'], True)
        rotar_simple(arbol, False)


def balancear(arbol):
    if arbol is not None:
        if altura(arbol['izq']) - altura(arbol['der']) == 2:
            if(altura(arbol['izq']['izq']) >= altura(arbol['izq']['der'])):
                rotar_simple(arbol, True)
            else:
                rotar_doble(arbol, True)
        elif altura(arbol['der']) - altura(arbol['izq']) == 2:
            if(altura(arbol['der']['der']) >= altura(arbol['der']['izq'])):
                rotar_simple(arbol, False)
            else:
                rotar_doble(arbol, False)


def arbol_vacio(arbol):
    return arbol['info'] is None


def preorden(arbol):
    if(arbol is not None):
        print(arbol['info'], arbol['altura'],
              arbol['izq']['info'] if arbol['izq'] else None,
              arbol['der']['info'] if arbol['der'] else None)
        preorden(arbol['izq'])
        preorden(arbol['der'])


def contar_heroes(arbol):
    contador = 0
    if(arbol is not None):
        if arbol['datos'] == False:
            contador += 1
        contador += contar_heroes(arbol['izq'])
        contador += contar_heroes(arbol['der'])
    return contador


def inorden(arbol):
    if(arbol is not None):
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])


def inorden_villano(arbol):
    if(arbol is not None):
        inorden_villano(arbol['izq'])
        if arbol['datos'] == True:
            print(arbol['info'])
        inorden_villano(arbol['der'])


def inorden_empieza_con(arbol, valor):
    if(arbol is not None):
        inorden_empieza_con(arbol['izq'], valor)
        # if arbol['info'].startswith(valor):
        if valor in arbol['info']:
            print(arbol['info'])
        inorden_empieza_con(arbol['der'], valor)


def postorden(arbol):
    if(arbol is not None):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])


def postorden_heroes(arbol):
    if(arbol is not None):
        postorden_heroes(arbol['der'])
        if arbol['datos'] == False:
            print(arbol['info'])
        postorden_heroes(arbol['izq'])


def busqueda(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux


def remplazar(arbol, anterior=None, primero=None):
    info, datos = None, None
    if arbol['der'] is None:
        info, datos = arbol['info'], arbol['datos']
        if anterior:
            anterior['der'] = arbol['izq']
        else:
            primero['izq'] = arbol['izq']
    else:
        info, datos = remplazar(arbol['der'], anterior=arbol)
    return info, datos


def eliminar_nodo(arbol, clave, previo=None, hijo=None):
    x, datos = None, None
    if arbol['info'] is not None:
        if clave < arbol['info']:
            x, datos = eliminar_nodo(arbol['izq'], clave, arbol, 'izq')
        elif clave > arbol['info']:
            x, datos = eliminar_nodo(arbol['der'], clave, arbol, 'der')
        else:
            x = arbol['info']
            datos = arbol['datos']
            if arbol['izq'] is None and arbol['der'] is not None:
                copiar_nodo(arbol['der'], arbol)
                # arbol['info'] = arbol['der']['info']
                # arbol['datos'] = arbol['der']['datos']
                # arbol['izq'] = arbol['der']['izq']
                # arbol['der'] = arbol['der']['der']
            elif arbol['der'] is None and arbol['izq'] is not None:
                copiar_nodo(arbol['izq'], arbol)
                # arbol['info'] = arbol['izq']['info']
                # arbol['datos'] = arbol['izq']['datos']
                # arbol['der'] = arbol['izq']['der']
                # arbol['izq'] = arbol['izq']['izq']
            elif arbol['izq'] is None and arbol['der'] is None:
                if previo is None:
                    arbol['info'] = None
                    arbol['datos'] = None
                else:
                    previo[hijo] = None
            else:
                info, datos = remplazar(arbol['izq'], primero=arbol)
                arbol['info'] = info
                arbol['datos'] = datos
        actualizar_altura(arbol)
        balancear(arbol)

    return x, datos


def por_nivel(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo['info'], nodo['izq']['info'] if nodo['izq'] else None, nodo['der']['info'] if nodo['der'] else None)
        if nodo['izq']:
            pendientes.arribo(nodo['izq'])
        if nodo['der']:
            pendientes.arribo(nodo['der'])


def crear_bosque(arbol, bosque1, bosque2,):
    if(arbol is not None):
        crear_bosque(arbol['izq'], bosque1, bosque2)
        if arbol['datos'] == True:
            insertar_nodo(bosque2, arbol['info'])
        else:
            insertar_nodo(bosque1, arbol['info'])
        crear_bosque(arbol['der'], bosque1, bosque2)

def contar_nodos(arbol):
    contador=0
    if (arbol is not None):
        contador+=1
        contador+=contar_nodos(arbol['der'])
        contador+=contar_nodos(arbol['izq'])
    return contador

def inorden_criaturas(arbol):
    if(arbol is not None):
        inorden_criaturas(arbol['izq'])
        print('Criatura: ',arbol['info'])
        print('Derrotada por: ',arbol['datos'].derrotadaPor)
        print('Capturada por: ',arbol['datos'].atrapadaPor)
        print('Datos adicionales: ',arbol['datos'].datosExtras)
        print()
        inorden_criaturas(arbol['der'])

def agregar_dato(arbol,elemento):
    encontrado=busqueda(arbol,elemento)
    if encontrado:
        dato=input('Ingrese el dato que desea agregar a la criatura: ').capitalize()
        encontrado['datos'].datosExtras=dato
        print()
        print(f'Nueva descripcion de {elemento}: ')
        print('Derrotado por: ',encontrado['datos'].derrotadaPor)
        print('Datos adicionales: ',encontrado['datos'].datosExtras)  
        print()    
    else:
        print('Criatura no encontrada')
        print()

def agregar_descripcion_a_todos(arbol):
    if(arbol is not None):
        agregar_descripcion_a_todos(arbol['izq'])
        elemento=arbol['info']
        print(elemento)
        agregar_dato(arbol,elemento)
        agregar_descripcion_a_todos(arbol['der'])

def tres_mayores(arbol,vector):
    if(arbol is not None):
        tres_mayores(arbol['izq'],vector)
        if (arbol['datos'][0] != '-') and arbol['datos'][0] not in vector:
            vector.append(arbol['datos'][0])
        tres_mayores(arbol['der'],vector)

def criaturas_derrotadas_heracles(arbol): 
    if arbol is not None:
        criaturas_derrotadas_heracles(arbol['izq'])
        if (arbol['datos'].derrotadaPor)=='Heracles':
            print(arbol['info'])
        criaturas_derrotadas_heracles(arbol['der'])

def criaturas_capturadas_heracles(arbol): 
    if arbol is not None:
        criaturas_capturadas_heracles(arbol['izq'])
        if (arbol['datos'].atrapadaPor)=='Heracles':
            print(arbol['info'])
        criaturas_capturadas_heracles(arbol['der'])

def criaturas_no_derrotadas(arbol):
    if arbol is not None:
        criaturas_no_derrotadas(arbol['izq'])
        if (arbol['datos'].derrotadaPor=='-'):
            print(arbol['info'])
        criaturas_no_derrotadas(arbol['der'])

def agregar_capturador(arbol,elemento):
    encontrado=busqueda(arbol,elemento)
    if encontrado:
        dato=input(f'Ingrese quien capturo a {elemento}: ').capitalize()
        encontrado['datos'].atrapadaPor=dato
        print()
        print(f'Nueva descripcion de {elemento}: ')
        print('Derrotado por: ',encontrado['datos'].derrotadaPor)
        print('Atrapada por: ',encontrado['datos'].atrapadaPor)  
        print()    
    else:
        print('Criatura no encontrada')
        print()

def modificar_info(arbol,elemento):
    encontrado=busqueda(arbol,elemento)
    if encontrado:
        dato=input(f'Ingrese nuevo nombre de {elemento}: ').capitalize()
        encontrado['info']=dato
        print()
        print(f'Nuevo nombre de {elemento}: ',encontrado['info'].title())
        print()    
    else:
        print('Criatura no encontrada')
        print()

        

        












