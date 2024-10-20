import P2

# Se agregan RUTs
P2.py_agregar_RUT("123456789", "Juan Perez", "Beauchef 851", "11/09/1973")
P2.py_agregar_RUT("987654321", "Maria Lopez", "La Exotica 456", "23/03/2001")

# Se marca como deudor
P2.py_numero_deudor("123456789")

# Se marca como no deudor
P2.py_numero_no_deudor("987654321")

# Se marca un nuevo RUT como no deudor (debería agregarlo al árbol)
P2.py_numero_no_deudor("555555555")

# Se comprueba si los RUTs son deudores o no
ruts = ["123456789", "987654321", "555555555"]

for rut in ruts:
    if P2.py_es_deudor(rut):
        print("DEUDOR")
    else:
        print("NO DEUDOR")

# Se guarda el árbol
P2.py_guardar_arbol("arbol_trie.txt")