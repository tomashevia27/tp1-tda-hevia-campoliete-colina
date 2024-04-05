from greedy import *

def generar_archivo_resultados():
    nombre_archivo_resultados = "Resultados Esperados Tests Propios.txt"
    archivo_resultados = open(nombre_archivo_resultados, 'w')

    for n in range(1000, 100001, 1000):
        nombre_archivo = str(n) + ".txt"
        archivo_resultados.write(nombre_archivo + "\n")
        arr = leer_archivo(nombre_archivo)
        sumatoria, _ = cal_sumatoria(arr)
        archivo_resultados.write(f"Coeficiente de impacto: {sumatoria}\n\n")

    archivo_resultados.close()

generar_archivo_resultados()
