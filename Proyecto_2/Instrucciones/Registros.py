from Abstract.Abstract import Expression

class Registros(Expression):

    def __init__(self, numero, nombre, fila, columna):
        self.nombre = nombre
        self.numero = numero
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()