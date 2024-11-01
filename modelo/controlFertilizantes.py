from modelo.productosDeControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, nombreProducto: str, registroIca: str, frecuenciaAplicacion: int, precioProducto: float, fechaUltimaAplicacion: str):
        super().__init__(nombreProducto, registroIca, frecuenciaAplicacion, precioProducto)
        self.__fechaUltimaAplicacion = fechaUltimaAplicacion

    @property
    def fechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion

    @fechaUltimaAplicacion.setter
    def fechaUltimaAplicacion(self, fechaUltimaAplicacion):
        if fechaUltimaAplicacion.strip():
            self.__fechaUltimaAplicacion = fechaUltimaAplicacion
        else:
            raise ValueError("Error: la fecha de última aplicación es obligatoria. Ingrese un valor válido.")

    def __str__(self):
        return f"ControlFertilizantes(nombreProducto={self.nombreProducto}, registroIca={self.registroIca}, frecuenciaAplicacion={self.frecuenciaAplicacion}, precioProducto={self.precioProducto}, fechaUltimaAplicacion={self.fechaUltimaAplicacion})"