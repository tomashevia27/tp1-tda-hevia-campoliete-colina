from tp1 import *
from sys import argv
from time import time

def main():
    inicio = time()
    arr=leer_archivo(argv[1])
    sumatoria,orden_optimo = cal_sumatoria_v2(arr)
    fin = time()
    print(f"Orden Optimo: {orden_optimo} \nCoeficiente minimo: {sumatoria}")
    print(f"Tiempo de ejecucion: {fin-inicio}")

main()