from collections import defaultdict

def find_frequent_elements(data):
    frequency = defaultdict(int)

    for item in data:
        hashed_item = hash(item)
        frequency[hashed_item] += 1

    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:5]  # Top 5 elementos más frecuentes

# Generar datos aleatorios
import random
random_data = [random.randint(1, 100) for _ in range(100000)]

# Encontrar elementos frecuentes
top_frequent = find_frequent_elements(random_data)
print("Top 5 elementos más frecuentes (hash):", top_frequent)
