import csv

TIEMPO = 0
PESO = 1

def leer_archivo(archivo):

    a = open(archivo)
    lector = csv.reader(a, delimiter=",")
    a.readline()

    arr = []

    for linea in lector:
        arr.append((int(linea[TIEMPO]), int(linea[PESO])))

    a.close()

    return arr

def ordenar_por_menor_relacion_tiempo_peso(arr):
    return sorted(arr, key= lambda batalla : batalla[TIEMPO]/batalla[PESO])

def cal_sumatoria(arr):
    arr = ordenar_por_menor_relacion_tiempo_peso(arr)
 
    sumatoria = 0
    tiempo_acumulado = 0
    
    for batalla in arr:
        tiempo_acumulado += batalla[TIEMPO]
        sumatoria += (batalla[PESO] * tiempo_acumulado)
    
    return sumatoria