from src.caminos_pcb import CaminosPCB
from src.decoradores import medir_tiempo
from src.graficos import graficar_tiempos

@medir_tiempo
def ejecutar_recursivo(pcb):
    return pcb.caminos_recursivo()

@medir_tiempo
def ejecutar_combinatorio(pcb):
    return pcb.caminos_combinatorio()

@medir_tiempo
def ejecutar_dinamico(pcb):
    return pcb.caminos_dinamico()

if __name__ == "__main__":
    tamanios = [(5, 5), (10, 10), (15, 15), (16,16)]  # Diferentes tamaños de grilla
    tiempos_recursivo = []
    tiempos_combinatorio = []
    tiempos_dinamico = []

    for n, m in tamanios:
        pcb = CaminosPCB(n, m)
        tiempos_recursivo.append(ejecutar_recursivo(pcb))
        tiempos_combinatorio.append(ejecutar_combinatorio(pcb))
        tiempos_dinamico.append(ejecutar_dinamico(pcb))

    tamanios_grilla = [n * m for n, m in tamanios]
    graficar_tiempos(tamanios_grilla, [tiempos_recursivo, tiempos_combinatorio, tiempos_dinamico], ["Recursivo", "Combinatorio", "Dinamico"])
