import random
import string
import time
import matplotlib.pyplot as plt

def radix_sort_strings(arr):
    max_length = len(max(arr, key=len))
    for position in range(max_length - 1, -1, -1):
        buckets = [[] for _ in range(256)]  # Asume caracteres ASCII
        for s in arr:
            char = ord(s[position]) if position < len(s) else 0 
            buckets[char].append(s)
        arr = [string for bucket in buckets for string in bucket]
    return arr

def generate_random_strings(num_strings, max_length):
    return [
        ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, max_length)))
        for _ in range(num_strings)
    ]

def measure_radix_sort_performance(num_elements = 10000):
    num_elements = int(num_elements)
    max_length = 15  
    data = generate_random_strings(num_elements, max_length)

    start_time = time.time()
    sorted_data = radix_sort_strings(data)
    end_time = time.time()
    sort_time = end_time - start_time

    print(f"Tiempo de ejecución para {num_elements} strings: {end_time - start_time:.4f} segundos")
    return data, sorted_data, sort_time

# Prueba

sizes = [1e4, 3e4, 5e4, 7e4, 9e4, 1e5, 1.3e5, 1.5e5, 1.7e5, 1.9e5]
times = []
for test in sizes:
    _, _, test_time = measure_radix_sort_performance(test)
    times.append(test_time)

plt.plot(sizes, times, marker='o')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Radix Sort para Datos Alfanúmericos')
plt.grid()
plt.show()

