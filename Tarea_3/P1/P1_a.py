import random
import time
import matplotlib.pyplot as plt

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort(key=lambda x: x[0])
    return pivot_candidates[1][1]

def quicksort(arr, low, high):
    if low < high:
        pivot_index = median_of_three(arr, low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        pivot_new_index = partition(arr, low, high)
        quicksort(arr, low, pivot_new_index - 1)
        quicksort(arr, pivot_new_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Prueba

sizes = [1e3, 5e3, 1e4, 5e4, 1e6, 3e6, 5e6, 7e6, 9e6, 3e7]
times = []
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(int(size))]
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    times.append(end_time - start_time)
plt.plot(sizes, times, marker='o')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('QuickSort con Mediana de Tres')
plt.grid()
plt.show()
