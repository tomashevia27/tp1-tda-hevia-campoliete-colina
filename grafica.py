
import matplotlib.pyplot as plt
import numpy as np
import csv

x=[]
y=[]
with open("TESTS/Mediciones.txt","r") as file:
    lector=csv.reader(file,delimiter=",")
    file.readline()
    for linea in lector:
        x.append(int(linea[0]))
        y.append(float(linea[1]))


figure,ax = plt.subplots()
ax.plot(x,y,color="Red",label="cal_sumatoria")
plt.title('Algoritmo de minima suma ponderada Greedy')
plt.xlabel('Cantidad de elementos en Arreglo')
plt.ylabel('Tiempo [ms]')
plt.grid(True)
ax.legend(loc='upper left')
plt.show()


