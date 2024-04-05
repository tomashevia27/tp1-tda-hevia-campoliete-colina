from random import randint
from sys import argv

MIN = 1
MAX = 999
SALTO = 1000
IDX_A = 1
IDX_B = 2

def generar_numero_aleatorio():
    return randint(MIN, MAX)

def generar_archivos(a, b):
    for n in range(int(a), int(b), SALTO):
        nombre_archivo = str(n) + ".txt"
        with open(nombre_archivo, 'w') as f:
            f.write("T_i,B_i\n")
            for _ in range(n):
                t_i = generar_numero_aleatorio()
                b_i = generar_numero_aleatorio()
                f.write(f"{t_i},{b_i}\n")

generar_archivos(argv[IDX_A], argv[IDX_B])
