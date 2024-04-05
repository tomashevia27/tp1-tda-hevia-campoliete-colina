from greedy import *
from time import time

def generar_mediciones():
    with open('Mediciones.txt','w') as file:
        file.write("Cantidad_de_elementos,Media_de_tiempo_de_ejecucion\n")
        for i in range(1000,100001,1000):
            arr=leer_archivo(str(i)+".txt")
            suma_de_tiempos=0
            for j in range(10):
                inicio=time()
                _ , _ = cal_sumatoria(arr)
                fin=time()
                suma_de_tiempos+=(fin-inicio)*1000
            file.write(str(i)+","+str(suma_de_tiempos/10)+"\n")

generar_mediciones()