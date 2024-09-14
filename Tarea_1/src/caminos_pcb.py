import math
from src.decoradores import medir_tiempo

class CaminosPCB:
    def __init__(self, n, m):
        self.n = n  # Número de filas
        self.m = m  # Número de columnas

    def caminos_recursivo(self, x=0, y=0):
        # Cuenta los caminos desde (0, 0) hasta (n-1, m-1) de forma recursiva
        if x == self.n - 1 and y == self.m - 1:
            return 1
        if x >= self.n or y >= self.m:
            return 0
        return self.caminos_recursivo(x + 1, y) + self.caminos_recursivo(x, y + 1)

    def caminos_combinatorio(self):
        # Cuenta los caminos utilizando combinatoria: C(N+M-2, N-1)
        return math.comb(self.n + self.m - 2, self.n - 1)
    
    def caminos_dinamico(self):
        # Cuenta los caminos utilizando programación dinámica
        dp = [[0 for _ in range(self.m)] for _ in range(self.n)]
        dp[0][0] = 1
        for i in range(self.n):
            for j in range(self.m):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[self.n - 1][self.m - 1]

    # Métodos decorados
    @medir_tiempo
    def ejecutar_recursivo(self):
        return self.caminos_recursivo()

    @medir_tiempo
    def ejecutar_combinatorio(self):
        return self.caminos_combinatorio()

    @medir_tiempo
    def ejecutar_dinamico(self):
        return self.caminos_dinamico()