from libc.stdlib cimport qsort, malloc, free
from libc.string cimport strcpy, strlen, strcmp, strtok, strcat

cdef struct TrieNode:
    char* palabra
    char* traduccion
    TrieNode* hijos[26]
    bint fin_palabra

cdef TrieNode* nuevo_nodo():
    cdef TrieNode* nodo = <TrieNode*> malloc(sizeof(TrieNode))
    nodo.palabra = NULL
    nodo.traduccion = NULL
    nodo.fin_palabra = 0
    for i in range(26):
        nodo.hijos[i] = NULL
    return nodo

cdef void borrar_nodo(TrieNode* pnode):
    if not pnode:
        return
    for i in range(26):
        if pnode.hijos[i]:
            borrar_nodo(pnode.hijos[i])
    if pnode.palabra:
        free(pnode.palabra)
    if pnode.traduccion:
        free(pnode.traduccion)
    free(pnode)

cdef int compare_strings(const void* a, const void* b) noexcept nogil:
    return strcmp(<const char*>a, <const char*>b)

cdef char* ordenar_traducciones(char* traduccion):
    
    # Se convierte el char* a un string de Python
    traduccion_str = traduccion.decode('utf-8')
    traducciones_py = traduccion_str.split(',')
    traducciones_py.sort()

    len_total = sum(len(t) for t in traducciones_py) + len(traducciones_py)  # + len por las comas

    cdef char* nueva_traduccion = <char*> malloc(len_total * sizeof(char))
    nueva_traduccion[0] = b'\0'[0] 

    for i, traduccion_part in enumerate(traducciones_py):
        strcat(nueva_traduccion, traduccion_part.encode('utf-8'))
        if i < len(traducciones_py) - 1:
            strcat(nueva_traduccion, b",")

    return nueva_traduccion

cdef int agregar_palabra(TrieNode* raiz, const char* palabra, char* traduccion):
    cdef TrieNode* nodo = raiz
    cdef int idx
    cdef int largo_palabra = strlen(palabra)

    # Se recorre cada letra de la palabra
    for i in range(largo_palabra):
        idx = ord(palabra[i]) - ord('a')  # Se convierte a índice basado en la posición en el alfabeto
        if not nodo.hijos[idx]:
            nodo.hijos[idx] = nuevo_nodo()
        nodo = nodo.hijos[idx]

    if nodo.fin_palabra:
        return 0  # La palabra ya existe
    nodo.fin_palabra = 1

    # Se ordena la traduccion antes de guardarla
    nodo.palabra = <char*> malloc((largo_palabra + 1) * sizeof(char))
    strcpy(nodo.palabra, palabra)

    nodo.traduccion = ordenar_traducciones(traduccion)

    return 1  # Palabra agregada exitosamente

cdef char* buscar_palabra(TrieNode* raiz, const char* palabra):
    cdef TrieNode* nodo = raiz
    cdef int idx
    cdef int largo_palabra = strlen(palabra)

    # Se recorre cada letra de la palabra
    for i in range(largo_palabra):
        idx = ord(palabra[i]) - ord('a')
        if not nodo.hijos[idx]:
            return NULL  # La palabra no existe
        nodo = nodo.hijos[idx]

    if nodo.fin_palabra:
        return nodo.traduccion
    else:
        return NULL  # La palabra no existe

# Función de prueba
def probar_trie():

    raiz = nuevo_nodo()

    agregar_palabra(raiz, b"like", b"amar,gustar,apreciar")
    agregar_palabra(raiz, b"cat", b"gato,felino,minino")
    agregar_palabra(raiz, b"dog", b"perro,canino,mascota")
    agregar_palabra(raiz, b"sigma", b"skibidi,toilet,pomni")

    palabras = [b"like", b"cat", b"dog", b"bird", b"programacionavanzadaEL4203", b"sigma"]

    for word in palabras:
        if buscar_palabra(raiz, word):
            print(f"Traducción de '{word.decode('utf-8')}' (ordenado): {buscar_palabra(raiz, word).decode('utf-8')}.")
        else:
            print(f"Palabra '{word.decode('utf-8')}' no encontrada.")
    
    borrar_nodo(raiz)

