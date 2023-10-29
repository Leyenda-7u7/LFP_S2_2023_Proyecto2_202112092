from Abstract.Abstract import Expression


class Sumar(Expression):
    def __init__(self, campo, fila, columna):
        self.campo = campo
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Lógica para sumar valores del campo
        pass

    def ejecutarT(self):
        # Lógica para imprimir la suma
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()