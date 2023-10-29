from Abstract.Abstract import Expression

class Datos(Expression):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Lógica para imprimir registros
        pass

    def ejecutarT(self):
        # Lógica para imprimir registros
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()