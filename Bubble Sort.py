# bubble sort XD
import random
import time

def generar_lista_aleatoria(n=1000):
    """Genera lista de n números aleatorios entre 1 y 10000, por que del 1 aal 1000 seria aburrido, le meto emocion haciendo que sean mil numeros entre el 1 al 10000"""
    return [random.randint(1, 10000) for _ in range(n)]

def bubble_sort(lista):
    """Implementación del algoritmo Bubble Sort"""
    n = len(lista)
    arr = lista.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

def main():
    print("=== BUBBLE SORT ===")
    print("Generando 1000 números aleatorios...")
    
    # Generar lista
    lista_original = generar_lista_aleatoria(1000)
    print(f"Lista original (primeros 10): {lista_original[:10]}")
    
    # Ordenar con Bubble Sort
    inicio = time.time()
    lista_ordenada = bubble_sort(lista_original)
    fin = time.time()
    
    # Verificar con sorted() de Python
    lista_python = sorted(lista_original)
    
    print(f"\nLista ordenada (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Verificación: {lista_ordenada == lista_python}")
    print(f"Mínimo: {lista_ordenada[0]}, Máximo: {lista_ordenada[-1]}")

if __name__ == "__main__":
    main()