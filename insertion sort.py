# insertion_sort.py
import random
import time

#como me encanta copiar y pegar el codigo de generacion de numeros

def generar_lista_aleatoria(n=1000):
    """Genera lista de n números aleatorios entre 1 y 10000"""
    return [random.randint(1, 10000) for _ in range(n)]

def insertion_sort(lista):
    """Implementación del algoritmo Insertion Sort"""
    arr = lista.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def main():
    print("=== INSERTION SORT ===")
    print("Generando 1000 números aleatorios...")
    
    # Generar lista
    lista_original = generar_lista_aleatoria(1000)
    print(f"Lista original (primeros 10): {lista_original[:10]}")
    
    # Ordenar con Insertion Sort
    inicio = time.time()
    lista_ordenada = insertion_sort(lista_original)
    fin = time.time()
    
    # Verificar con sorted() de Python
    lista_python = sorted(lista_original)
    
    print(f"\nLista ordenada (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Verificación: {lista_ordenada == lista_python}")
    print(f"Mínimo: {lista_ordenada[0]}, Máximo: {lista_ordenada[-1]}")

if __name__ == "__main__":
    main()