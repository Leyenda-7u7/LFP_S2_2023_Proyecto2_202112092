from Abstract.Abstract import Expression

class Conteo(Expression):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Implementa la lógica de conteo aquí
        pass

    def ejecutarT(self):
        # Implementa la ejecución de la instrucción aquí
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()