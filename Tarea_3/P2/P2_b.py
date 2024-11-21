def detect_duplicates(file_path):
    seen_hashes = set()
    duplicates = set()

    with open(file_path, 'r') as file:
        for line in file:
            hashed_line = hash(line.strip())
            if hashed_line in seen_hashes:
                duplicates.add(line.strip())
            else:
                seen_hashes.add(hashed_line)

    return duplicates

# Crear un archivo de ejemplo
with open('example.txt', 'w') as f:
    f.write("line1\nline2\nline3\nline2\nline1\nline4\n")
    f.write("skibidi\ndobdob\nyes\nskibidi\ndibdib\n")
    f.write("quick\nradix\ncomb\nbubble\nradix\nbubble\nsort\n")

# Detectar duplicados
duplicates = detect_duplicates('example.txt')
print("Duplicados encontrados:", duplicates)
