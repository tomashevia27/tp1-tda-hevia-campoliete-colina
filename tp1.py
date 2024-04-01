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

"""
def ordenar_por_mayor_peso(arr):
    return sorted(arr, key= lambda batalla : batalla[PESO], reverse= True)

def ordenar_por_menor_tiempo(arr):
    return sorted(arr, key= lambda batalla : batalla[TIEMPO])
"""

def ordenar_por_menor_relacion_tiempo_peso(arr):
    return sorted(arr, key= lambda batalla : batalla[TIEMPO]/batalla[PESO])

def cal_sumatoria(arr):
    arr = ordenar_por_menor_relacion_tiempo_peso(arr)
 
    sumatoria = 0
    tiempo_acumulado = 0
    orden_batallas = []
    
    for batalla in arr:
        tiempo_acumulado += batalla[TIEMPO]
        sumatoria += batalla[PESO] * tiempo_acumulado
        orden_batallas.append(batalla[IDX])
    
    return sumatoria, orden_batallas

"""
Primero, definamos claramente lo que queremos demostrar. Queremos demostrar que ordenar las tuplas 
por ti/bi de forma ascendente minimiza la sumatoria desde 1 hasta n de bi * Fi, donde Fi es la suma 
de todos los t anteriores incluido el actual.

Luego, podemos proceder con una demostración por contradicción. Supongamos que hay una inversión en 
el orden óptimo de las tuplas. Es decir, hay dos tuplas (ti, bi) y (tj, bj) tales que i < j pero 
ti/bi > tj/bj.

Ahora, vamos a comparar los términos que involucran a estas dos tuplas en la sumatoria:

Para la tupla (ti, bi):
Su contribución a la sumatoria es bi * (t1 + t2 + ... + ti)

Para la tupla (tj, bj):
Su contribución a la sumatoria es bj * (t1 + t2 + ... + ti + tj)

La contribución de ambas es bi*t1 + bi*t2 + ... + bi*ti + bj*t1 + bj*t2 + ... + bj*ti + bj*tj

Ahora, ¿cuál sería la contribución si intercambiamos las tuplas?

Para la tupla (tj, bj):
Su contribución a la sumatoria es bj * (t1 + t2 + ... + tj)

Para la tupla (ti, bi):
Su contribución a la sumatoria es bi * (t1 + t2 + ... + tj + ti)

La contribución de ambas es bj*t1 + bj*t2 + ... + bj*tj + bi*t1 + bi*t2 + ... + bi*tj + bi*ti

Todos los términos de ambas contribuciones son iguales salvo por bj*ti (en la primera contribución)
y bi*tj (en la segunda).

Pero supusimos inicialmente que ti/bi > tj/bj, entonces bj * ti > bi * tj. Esto implica que al 
intercambiar estas dos tuplas en el orden óptimo, obtendremos una sumatoria menor, lo que contradice
la suposición de que el orden original era óptimo. Por lo tanto, no puede haber 
una inversión en el orden óptimo, lo que significa que ordenar las tuplas por ti/bi de forma 
ascendente es de hecho la solución óptima.










arr = [(5,2),(4,1),(8,5),(9,9),(2,3)]
optimo = [(2,3),(9,9),(8,5),(5,2),(4,1)]
sumatoria = 3*2 + 9*11 + 5*19 + 2*24 + 1*28 = 6 + 99 + 95 + 48 + 28 = 276

inversiones = [(2,3),(9,9),(5,2),(8,5),(4,1)]
sumatoria_chota = 3*2 + 9*11 + 2*16 + 5*24 + 1*28 = 6 + 99 + 32 + 120 + 28 = 285

Para la tupla (5, 2):
ti/bi = 5/2 = 2.5
Su contribución a la sumatoria es 2 * (2+9+5) = 2*16+32
Su contribución a la sumatoria es bi * (t1+t2+t3) = 2*16+32

Para la tupla (8, 5):
tj/bj = 8/5 = 1.6
Su contribución a la sumatoria es 5 * (2+9+5+8) = 5*24 = 120


"""