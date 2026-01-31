#bubble sort (otra vez)

import random
import time

def generar_lista_aleatoria(n=1000):
    return [random.randint(1, 10000) for _ in range(n)]

def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)
    
    for i in range(n-1, 0, -1):
        ordenado = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ordenado = False
        if ordenado:
            break
    
    return arr

def main():
    print("=== BUBBLE SORT OPTIMIZADO ===")
    print("Generando 1000 números aleatorios...")
    
    lista_original = generar_lista_aleatoria(1000)
    print(f"Primeros 10: {lista_original[:10]}")
    
    inicio = time.time()
    lista_ordenada = bubble_sort(lista_original)
    tiempo = time.time() - inicio
    
    print(f"\nOrdenados (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Verificado: {lista_ordenada == sorted(lista_original)}")
    print(f"Rango: [{lista_ordenada[0]}, {lista_ordenada[-1]}]")

if __name__ == "__main__":
    main()
