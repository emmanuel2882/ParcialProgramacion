from modelo.ProductoDeControl import ProductoDeControl
class ControlDePlagas(ProductoDeControl):
    def __init__(self, nombre, valor, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, valor, registro_ica, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia

    def __str__(self):
        return (f"{super().__str__()}, Periodo de Carencia: {self.periodo_carencia} días")
