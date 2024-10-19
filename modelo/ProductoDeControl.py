from modelo.Producto import Producto

class ProductoDeControl(Producto):
    def __init__(self, nombre, valor, registro_ica, frecuencia_aplicacion):
        super().__init__(nombre, valor)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion

    def __str__(self):
        return (f"{super().__str__()}, Registro ICA: {self.registro_ica}, "
                f"Frecuencia de Aplicación: {self.frecuencia_aplicacion}")
