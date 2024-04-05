
import matplotlib.pyplot as plt
import numpy as np
import csv

x=[]
y=[]
with open("TESTS/Mediciones.txt","r") as file:
    lector=csv.reader(file,delimiter=",")
    file.readline()
    for linea in lector:
        x.append(linea[0])
        y.append(linea[1])
    

plt.plot(x,y,color='blue')

# plt.plot(x,y1, color="green")

plt.title('ALgoritmo de minima suma ponderada Greedy')
plt.xlabel('Cantidad de elementos en Arreglo')
plt.ylabel('Tiempo [ms]')
plt.show()


