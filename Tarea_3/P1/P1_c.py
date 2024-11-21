import random
import time
import matplotlib.pyplot as plt

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False 
            i += 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def compare_sorts(size=1000):
    size = int(size)  # Número de elementos
    arr = [random.randint(0, 10000) for _ in range(size)]

    # CombSort
    comb_arr = arr.copy()
    start_time = time.time()
    comb_sort(comb_arr)
    comb_time = time.time() - start_time

    # Bubble Sort
    bubble_arr = arr.copy()
    start_time = time.time()
    bubble_sort(bubble_arr)
    bubble_time = time.time() - start_time

    # Verificar que los resultados sean iguales
    assert comb_arr == bubble_arr, "Los algoritmos no produjeron el mismo resultado"

    print(f"Tiempo de CombSort: {comb_time:.4f} segundos")
    print(f"Tiempo de Bubble Sort: {bubble_time:.4f} segundos")
    print(f"CombSort es {bubble_time / comb_time:.2f} veces más rápido que Bubble Sort")

    return comb_time, bubble_time

# Prueba

sizes = [1e3, 5e3, 1e4, 1.5e4, 1.7e4, 2e4, 3e4, 5e4]
comb_times = []
bubble_times = []
for test in sizes:
    comb_time, bubble_time = compare_sorts(test)
    comb_times.append(comb_time)
    bubble_times.append(bubble_time)

plt.plot(sizes, comb_times, marker='o', label='Comb Sort')
plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Comb Sort V/S Bubble Sort')
plt.legend()
plt.grid()
plt.show()