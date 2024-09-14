import matplotlib.pyplot as plt

def graficar_tiempos(n, tiempos, etiquetas):
    for tiempo, etiqueta in zip(tiempos, etiquetas):
        plt.plot(n, tiempo, label=etiqueta, marker='o')
    plt.xlabel("Tamaño de la grilla (NxM)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de tiempos de ejecución")
    plt.legend()
    plt.savefig('tiempos_ejecucion.svg')
    plt.savefig('tiempos_ejecucion.png')
    plt.show()