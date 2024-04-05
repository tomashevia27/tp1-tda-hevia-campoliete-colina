from greedy import *
from sys import argv
from time import time

IDX_ARCHIVO = 1
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def main():
    
    arr = leer_archivo(argv[IDX_ARCHIVO])
    inicio = time()
    sumatoria, orden_optimo = cal_sumatoria(arr)
    fin = time()

    print(RED + BOLD + "Orden óptimo:" + END + f" {orden_optimo}")
    print(RED + BOLD + "Coeficiente de impacto:" + END + f" {sumatoria}")
    print(RED + BOLD + "Tiempo de ejecución:" + END + f" {(fin-inicio) * 1000} milisegundos")

main()
