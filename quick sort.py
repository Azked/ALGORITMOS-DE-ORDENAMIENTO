#quick sort
import random
import time

#se me olvido añadir algo en merge sort, ni que fuera importante

def generar_lista_aleatoria(n=1000):
    """Genera lista de n números aleatorios entre 1 y 10000"""
    return [random.randint(1, 10000) for _ in range(n)]

def quick_sort(lista):
    """Implementación del algoritmo Quick Sort"""
    if len(lista) <= 1:
        return lista
    
    pivot = lista[-1]
    menores = [x for x in lista[:-1] if x <= pivot]
    mayores = [x for x in lista[:-1] if x > pivot]
    
    return quick_sort(menores) + [pivot] + quick_sort(mayores)

def main():
    print("=== QUICK SORT ===")
    print("Generando 1000 números aleatorios...")
    
    # Generar lista
    lista_original = generar_lista_aleatoria(1000)
    print(f"Lista original (primeros 10): {lista_original[:10]}")
    
    # Ordenar con Quick Sort
    inicio = time.time()
    lista_ordenada = quick_sort(lista_original)
    fin = time.time()
    
    # Verificar con sorted() de Python
    lista_python = sorted(lista_original)
    
    print(f"\nLista ordenada (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Verificación: {lista_ordenada == lista_python}")
    print(f"Mínimo: {lista_ordenada[0]}, Máximo: {lista_ordenada[-1]}")

if __name__ == "__main__":
    main()