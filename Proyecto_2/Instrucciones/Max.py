from Abstract.Abstract import Expression

class Max(Expression):
    def __init__(self, campo, fila, columna):
        self.campo = campo
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Lógica para encontrar el valor máximo del campo
        pass

    def ejecutarT(self):
        # Lógica para imprimir el valor máximo
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()