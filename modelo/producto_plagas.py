from modelo.productosDeControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombreProducto: str, registroIca: str, frecuenciaAplicacion: int, precioProducto: float, periodoCarencia: int):
        super().__init__(nombreProducto, registroIca, frecuenciaAplicacion, precioProducto)
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia

    @periodoCarencia.setter
    def periodoCarencia(self, periodoCarencia):
        if periodoCarencia > 0:
            self.__periodoCarencia = periodoCarencia
        else:
            raise ValueError("Error: el periodo de carencia debe ser mayor que cero. Por favor ingrese un valor positivo.")

    def __str__(self):
        return f"ControlPlagas(nombreProducto={self.nombreProducto}, registroIca={self.registroIca}, frecuenciaAplicacion={self.frecuenciaAplicacion}, precioProducto={self.precioProducto}, periodoCarencia={self.periodoCarencia})"