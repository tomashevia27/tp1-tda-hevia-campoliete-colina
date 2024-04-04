from funciones import *
from sys import argv
from time import time

def main():
    
    inicio = time()
    arr = leer_archivo(argv[1])
    sumatoria, orden_optimo = cal_sumatoria(arr)
    fin = time()

    print(f"Orden óptimo: {orden_optimo}\nCoeficiente mínimo: {sumatoria}")
    print(f"Tiempo de ejecución: {(fin-inicio) * 1000} milisegundos")

main()

