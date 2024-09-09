import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos")
        resultado = fin - inicio
        return resultado
    return wrapper
