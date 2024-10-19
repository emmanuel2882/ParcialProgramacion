from modelo.ProductoDeControl     import ProductoDeControl
class ControlDeFertilizantes(ProductoDeControl):
    def __init__(self, nombre, valor, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, valor, registro_ica, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return (f"{super().__str__()}, Fecha Última Aplicación: {self.fecha_ultima_aplicacion}")
