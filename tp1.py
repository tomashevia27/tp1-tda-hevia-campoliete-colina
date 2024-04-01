import csv

TIEMPO = 0
PESO = 1

def leer_archivo(archivo):

    a = open(archivo)
    lector = csv.reader(a, delimiter=",")
    a.readline()

    arr = []
    i = 1 

    for linea in lector:
        arr.append((int(linea[TIEMPO]), int(linea[PESO]), i))
        i += 1

    a.close()

    return arr


def cal_sumatoria_v2(arr):
    arr=sorted(arr, key=lambda valor: valor[1]/valor[0], reverse=True)
    # arr=sorted(arr, key=lambda valor: valor[0]/valor[1])
 
    sumatoria = 0
    tiempo_acumulado = 0
    orden_batalla = []
    
    for batalla in arr:
        tiempo_acumulado += batalla[0]
        sumatoria += tiempo_acumulado * batalla[1]
        orden_batalla.append(batalla[2])
    
    return sumatoria, orden_batalla

