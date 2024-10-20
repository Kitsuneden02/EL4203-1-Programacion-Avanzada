from libc.stdlib cimport malloc, free, realloc
from libc.string cimport strcpy, strlen, memset
from libc.stdio cimport FILE, fopen, fclose, fprintf, printf

cdef enum Status:
    NO_DEUDOR = 0
    DEUDOR = 1

cdef struct UserInfo:
    char* nombre
    char* direccion
    char* fecha_nacimiento
    Status status

cdef struct TrieNode:
    char digit
    UserInfo* info
    TrieNode** children
    int children_count

cdef TrieNode* nuevo_nodo(char digit):
    cdef TrieNode* node = <TrieNode*>malloc(sizeof(TrieNode))
    if node == NULL:
        return NULL
    node.digit = digit
    node.info = NULL
    node.children = NULL
    node.children_count = 0
    return node

cdef void borrar_nodo(TrieNode* pnode):
    cdef int i
    if pnode == NULL:
        return
    
    if pnode.info != NULL:
        free(pnode.info.nombre)
        free(pnode.info.direccion)
        free(pnode.info.fecha_nacimiento)
        free(pnode.info)
    
    for i in range(pnode.children_count):
        borrar_nodo(pnode.children[i])
    
    if pnode.children != NULL:
        free(pnode.children)
    
    free(pnode)

cdef TrieNode* buscar_nodo(TrieNode* root, const char* RUT):
    cdef TrieNode* current = root
    cdef int i, j, len_RUT = strlen(RUT)
    cdef char digit

    for i in range(len_RUT):
        digit = RUT[i]
        for j in range(current.children_count):
            if current.children[j].digit == digit:
                current = current.children[j]
                break
        else:
            return NULL  # RUT no encontrado
    return current

cdef int agregar_RUT(TrieNode* root, const char* RUT, const char* nombre, const char* direccion, const char* fecha_nacimiento):
    cdef TrieNode* current = root
    cdef int i, j, len_RUT = strlen(RUT)
    cdef char digit

    for i in range(len_RUT):
        digit = RUT[i]
        for j in range(current.children_count):
            if current.children[j].digit == digit:
                current = current.children[j]
                break
        else:
            new_node = nuevo_nodo(digit)
            if new_node == NULL:
                return 0
            current.children_count += 1
            current.children = <TrieNode**>realloc(current.children, current.children_count * sizeof(TrieNode*))
            if current.children == NULL:
                free(new_node)
                return 0
            current.children[current.children_count - 1] = new_node
            current = new_node

    if current.info == NULL:
        current.info = <UserInfo*>malloc(sizeof(UserInfo))
        if current.info == NULL:
            return 0
        current.info.nombre = <char*>malloc((strlen(nombre) + 1) * sizeof(char))
        current.info.direccion = <char*>malloc((strlen(direccion) + 1) * sizeof(char))
        current.info.fecha_nacimiento = <char*>malloc((strlen(fecha_nacimiento) + 1) * sizeof(char))
        if current.info.nombre == NULL or current.info.direccion == NULL or current.info.fecha_nacimiento == NULL:
            free(current.info.nombre)
            free(current.info.direccion)
            free(current.info.fecha_nacimiento)
            free(current.info)
            current.info = NULL
            return 0
        strcpy(current.info.nombre, nombre)
        strcpy(current.info.direccion, direccion)
        strcpy(current.info.fecha_nacimiento, fecha_nacimiento)
        current.info.status = NO_DEUDOR
        return 1
    return 0

cdef void numero_no_deudor(TrieNode* pnode, const char* RUT):
    cdef TrieNode* current = pnode
    cdef int i, j, len_RUT = strlen(RUT)
    cdef char digit

    for i in range(len_RUT):
        digit = RUT[i]
        for j in range(current.children_count):
            if current.children[j].info != NULL and current.children[j].info.nombre[0] == digit:
                current = current.children[j]
                break
        else:
            # Si el RUT no existe, se agrega
            agregar_RUT(pnode, RUT, "", "", "")
            return

    if current.info != NULL:
        current.info.status = NO_DEUDOR

cdef void numero_deudor(TrieNode* pnode, const char* RUT):
    cdef TrieNode* current = pnode
    cdef int i, j, len_RUT = strlen(RUT)
    cdef char digit

    for i in range(len_RUT):
        digit = RUT[i]
        for j in range(current.children_count):
            if current.children[j].digit == digit:
                current = current.children[j]
                break
        else:
            # Si el RUT no existe, lo agregamos
            agregar_RUT(pnode, RUT, "", "", "")
            current = current.children[current.children_count - 1]

    if current.info != NULL:
        current.info.status = DEUDOR

cdef void borrar_RUT(TrieNode* pnode, const char* RUT):
    cdef TrieNode* current = pnode
    cdef int i, j, len_RUT = strlen(RUT)
    cdef char digit

    for i in range(len_RUT):
        digit = RUT[i]
        for j in range(current.children_count):
            if current.children[j].info != NULL and current.children[j].info.nombre[0] == digit:
                current = current.children[j]
                break
        else:
            # Si el RUT no existe, no se hace nada
            return

    if current.info != NULL:
        free(current.info.nombre)
        free(current.info.direccion)
        free(current.info.fecha_nacimiento)
        free(current.info)
        current.info = NULL

cdef int es_deudor(TrieNode* root, const char* RUT):
    cdef TrieNode* node = buscar_nodo(root, RUT)
    if node != NULL and node.info != NULL:
        return node.info.status == DEUDOR
    return -1  # RUT no encontrado

cdef void guardar_arbol_recursivo(TrieNode* node, FILE* file, char* current_RUT, int depth):
    cdef int i
    if node == NULL:
        return
    
    if node.digit != 0:  # Si no es el nodo raíz
        current_RUT[depth - 1] = node.digit
    
    if node.info != NULL:
        current_RUT[depth] = 0  # Null terminator
        fprintf(file, "%s,%s,%s,%s,%d\n", current_RUT, node.info.nombre, node.info.direccion, 
                node.info.fecha_nacimiento, node.info.status)
    
    for i in range(node.children_count):
        guardar_arbol_recursivo(node.children[i], file, current_RUT, depth + 1)

cdef void guardar_arbol(TrieNode* root, const char* filename):
    cdef FILE* file = fopen(filename, "w")
    cdef char current_RUT[9]  # Suponiendo que el RUT no tiene más de 9 dígitos
    
    if file == NULL:
        printf("Error al abrir el archivo para escritura.\n")
        return
    
    memset(current_RUT, 0, sizeof(current_RUT))
    guardar_arbol_recursivo(root, file, current_RUT, 0)
    fclose(file)

# Funciones de interfaz Python
def py_agregar_RUT(RUT, nombre, direccion, fecha_nacimiento):
    global root
    return agregar_RUT(root, RUT.encode('utf-8'), nombre.encode('utf-8'), direccion.encode('utf-8'), fecha_nacimiento.encode('utf-8'))

def py_numero_no_deudor(RUT):
    global root
    numero_no_deudor(root, RUT.encode('utf-8'))

def py_numero_deudor(RUT):
    global root
    numero_deudor(root, RUT.encode('utf-8'))

def py_borrar_RUT(RUT):
    global root
    borrar_RUT(root, RUT.encode('utf-8'))

def py_es_deudor(RUT):
    global root
    return es_deudor(root, RUT.encode('utf-8'))

def py_guardar_arbol(filename):
    global root
    guardar_arbol(root, filename.encode('utf-8'))

cdef TrieNode* root = nuevo_nodo(0)