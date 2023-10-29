from Abstract.Abstract import Expression

class Contarsi(Expression):
    def __init__(self, campo, valor, fila, columna):
        self.campo = campo
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        # Lógica para contar registros según el campo y valor
        pass

    def ejecutarT(self):
        # Lógica para imprimir la cantidad de registros
        pass

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()