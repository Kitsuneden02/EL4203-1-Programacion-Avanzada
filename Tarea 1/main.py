from src.caminos_pcb import CaminosPCB
from src.graficos import graficar_tiempos

if __name__ == "__main__":
    tamanios = [(5, 5), (10, 10), (12, 12), (14,14), (15, 15)]  # Diferentes tamaños de grilla
    tiempos_recursivo = []
    tiempos_combinatorio = []
    tiempos_dinamico = []

    for n, m in tamanios:
        pcb = CaminosPCB(n, m)
        tiempos_recursivo.append(pcb.ejecutar_recursivo()[1])
        tiempos_combinatorio.append(pcb.ejecutar_combinatorio()[1])
        tiempos_dinamico.append(pcb.ejecutar_dinamico()[1])

    tamanios_grilla = [n * m for n, m in tamanios]
    graficar_tiempos(tamanios_grilla, [tiempos_recursivo, tiempos_combinatorio, tiempos_dinamico], \
                     ["Recursivo", "Combinatorio", "Dinamico"])
