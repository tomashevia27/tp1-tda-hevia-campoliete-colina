import csv

TIEMPO = 0
PESO = 1
IDX = 2

def leer_archivo(archivo):

    a = open(archivo)
    lector = csv.reader(a, delimiter=",")
    a.readline()

    arr = []

    for i, linea in enumerate(lector):
        arr.append((int(linea[TIEMPO]), int(linea[PESO]), i+1))

    a.close()

    return arr

def ordenar_por_menor_relacion_tiempo_peso(arr):
    return sorted(arr, key= lambda batalla : batalla[TIEMPO]/batalla[PESO])

def cal_sumatoria(arr):
    """funcion que calcula la menor sumatoria posible dado un set de datos cuyos elementos
    son(t,b) devuelve dicha suma y el orden optimo en el que se usan los elementos"""

    arr = ordenar_por_menor_relacion_tiempo_peso(arr)
 
    sumatoria = 0
    tiempo_acumulado = 0
    orden_batallas = []
    
    for batalla in arr:
        tiempo_acumulado += batalla[TIEMPO]
        sumatoria += batalla[PESO] * tiempo_acumulado
        orden_batallas.append(batalla[IDX])
    
    return sumatoria, orden_batallas