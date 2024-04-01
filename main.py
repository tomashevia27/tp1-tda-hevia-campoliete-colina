from tp1 import *
from sys import argv
from time import time

def lineal(arr):
    sumatoria=0
    for _,peso,_ in arr:
        sumatoria+=peso
    return 


def main():
    inicio = time()
    arr = leer_archivo(argv[1])
    sumatoria, orden_optimo = cal_sumatoria(arr)
    fin = time()

    inicio2=time()
    arr = leer_archivo(argv[1])
    lineal(arr)
    fin2=time()

    print(f"Orden óptimo: {orden_optimo}\nCoeficiente mínimo: {sumatoria}")
    print(f"Tiempo de ejecución: {(fin-inicio) * 1000} milisegundos")
    print(f"lineal:{(fin2-inicio2)*1000}")

main()


