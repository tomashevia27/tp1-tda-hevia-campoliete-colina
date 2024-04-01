import csv
import random
from sys import argv

def generar_numero():
    return random.randint(1, 999)

def generar_archivo():
    num_entradas = int(argv[1])
    nombre_archivo = argv[1] + ".txt"

    with open(nombre_archivo, 'w') as f:
        f.write("T_i,B_i\n")
        for _ in range(num_entradas):
            t_i = generar_numero()
            b_i = generar_numero()
            f.write(f"{t_i},{b_i}\n")

generar_archivo()

