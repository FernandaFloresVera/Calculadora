import numpy as np
from scipy import stats
import os.path

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning) #Coman q evita las advertencias

def calcula_estadisticas(numeros):
    media = np.mean(numeros)
    mediana = np.median(numeros)
    moda = stats.mode(numeros)
    return media, mediana, moda

def guardar_resultados(archivo, media, mediana, moda):
    with open(archivo, 'a') as f:
        f.write(f"Media: {media}\n")
        f.write(f"Mediana: {mediana}\n")
        f.write(f"Moda: {moda.mode[0]}, Frecuencia: {moda.count[0]}\n")
        f.write('\n')

def main():
    numeros = [int(x) for x in input("Introduce una sucesión de números separados por espacios: ").split()]
    media, mediana, moda = calcula_estadisticas(numeros)
    print(f"Media: {media}, Mediana: {mediana}, Moda: {moda.mode[0]}, Frecuencia: {moda.count[0]}")
    
    archivo = input("Ingresa el nombre del archivo con el que se guardaran tus datos ('name.txt'): ")
    
    if not archivo.endswith('.txt'):
        archivo = archivo + '.txt'
    
    if not os.path.exists(archivo):
        print(f"Creando archivo {archivo}...")
    
    guardar_resultados(archivo, media, mediana, moda)
    print(f"Exitosamente guardado en {archivo}.")

if __name__ == '__main__':
    main()
