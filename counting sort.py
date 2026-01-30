# counting sort
import random
import time

def generar_lista_aleatoria(n=1000):
    """Genera lista de n números aleatorios entre 1 y 10000"""
    return [random.randint(1, 10000) for _ in range(n)]

def counting_sort(lista):
    """
    Implementación del algoritmo Counting Sort
    Funciona bien para números en un rango específico
    """
    if not lista:
        return []
    
    # Encontrar el valor máximo
    max_val = max(lista)
    
    # Crear array de conteo
    count = [0] * (max_val + 1)
    
    # Contar ocurrencias
    for num in lista:
        count[num] += 1
    
    # Reconstruir lista ordenada
    sorted_list = []
    for i in range(len(count)):
        sorted_list.extend([i] * count[i])
    
    return sorted_list

def main():
    print("=== COUNTING SORT ===")
    print("Generando 1000 números aleatorios...")
    
    # Generar lista
    lista_original = generar_lista_aleatoria(1000)
    print(f"Lista original (primeros 10): {lista_original[:10]}")
    
    # Ordenar con Counting Sort
    inicio = time.time()
    lista_ordenada = counting_sort(lista_original)
    fin = time.time()
    
    # Verificar con sorted() de Python
    lista_python = sorted(lista_original)
    
    print(f"\nLista ordenada (primeros 10): {lista_ordenada[:10]}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Verificación: {lista_ordenada == lista_python}")
    print(f"Mínimo: {lista_ordenada[0]}, Máximo: {lista_ordenada[-1]}")

if __name__ == "__main__":
    main()













#texto de relleno