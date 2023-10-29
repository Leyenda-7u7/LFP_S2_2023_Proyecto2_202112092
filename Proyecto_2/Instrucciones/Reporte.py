from Abstract.Abstract import Expression

class Reporte(Expression):
    def __init__(self, titulo, fila, columna):
        self.titulo = titulo
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Lógica para generar el archivo HTML con el reporte
        pass

    def ejecutarT(self):
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()