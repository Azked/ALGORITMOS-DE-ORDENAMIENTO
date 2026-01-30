#merge sort
import random
import time

def generar_lista_aleatoria(n=1000):
    """Genera lista de n números aleatorios entre 1 y 10000"""
    return [random.randint(1, 10000) for _ in range(n)]

def merge_sort(lista):
    """Implementación del algoritmo Merge Sort"""
    if len(lista) <= 1:
        return lista
    
    mid = len(lista) // 2
    left_half = merge_sort(lista[:mid])
    right_half = merge_sort(lista[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """Función auxiliar para combinar dos listas ordenadas"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def main():
    print("=== MERGE SORT ===")
    print("Generando 1000 números aleatorios...")
    
    # Generar lista
    lista_original = generar_lista_aleatoria(1000)
    print(f"Lista original (primeros 10): {lista_original[:10]}")
    
    # Ordenar con Merge Sort
    inicio = time.time()
    lista_ordenada = merge_sort(lista_original)
    fin = time.time()
    
    # Verificar con sorted() de Python
    lista_python = sorted(lista_original)
    
    print(f"\nLista ordenada (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Verificación: {lista_ordenada == lista_python}")
    print(f"Mínimo: {lista_ordenada[0]}, Máximo: {lista_ordenada[-1]}")

if __name__ == "__main__":
    main()