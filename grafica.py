
import matplotlib.pyplot as plt
import csv

x=[]
y=[]
x2=[]
y2=[]
with open("TESTS/Mediciones.txt","r") as file:
    lector=csv.reader(file,delimiter=",")
    file.readline()
    for linea in lector:
        x.append(int(linea[0]))
        y.append(float(linea[1]))

with open("TESTS/Mediciones_lineal.txt") as file:
    lector=csv.reader(file,delimiter=",")
    file.readline()
    for linea in lector:
        x2.append(int(linea[0]))
        y2.append(float(linea[1]))


figure,ax = plt.subplots()
ax.plot(x,y,color="Red",label="cal_sumatoria")
ax.legend(loc='upper left')

ax.plot(x2,y2,color="Blue",label="encontrar_maximo")
ax.legend(loc='upper left')

plt.title('Algoritmo de Mínima Suma Ponderada Greedy')
plt.xlabel('Cantidad de elementos en Arreglo')
plt.ylabel('Tiempo [ms]')
plt.grid(True)
plt.show()


