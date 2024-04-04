
import matplotlib.pyplot as plt
import numpy as np

# y1=[1.4944,6.3301,11.5301,22.7956,45.4601,73.5752,107.2695,119.2493]

x = [1000, 5000, 10000, 20000, 40000, 60000, 80000, 100000]
y = [2.3401, 9.3862, 19.2460, 37.9420, 79.4304, 132.1209, 179.0515, 213.1779]

# plt.scatter(x,y,color="red",label="Greedy")
plt.plot(x,y,color='blue')

# plt.plot(x,y1, color="green")

plt.title('ALgoritmo de minima suma ponderada Greedy')
plt.xlabel('Cantidad de elementos en Arreglo')
plt.ylabel('Tiempo [ms]')
plt.grid(True)
plt.show()


