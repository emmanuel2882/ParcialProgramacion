class ProductoControl:
    def __init__(self, nombreProducto: str, registroIca: str, frecuenciaAplicacion: int, precioProducto: float):
        self.__nombreProducto = nombreProducto
        self.__registroIca = registroIca
        self.__frecuenciaAplicacion = frecuenciaAplicacion
        self.__precioProducto = precioProducto

    # Propiedades con sus validaciones
    @property
    def nombreProducto(self):
        return self.__nombreProducto

    @nombreProducto.setter
    def nombreProducto(self, nombreProducto):
        if not nombreProducto.strip():
            raise ValueError("Error: nombre del producto vacío. Ingrese un nombre válido.")
        self.__nombreProducto = nombreProducto

    @property
    def registroIca(self):
        return self.__registroIca

    @registroIca.setter
    def registroIca(self, registroIca):
        if not registroIca.strip():
            raise ValueError("Error: registro ICA vacío. Ingrese un registro válido.")
        self.__registroIca = registroIca

    @property
    def frecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion

    @frecuenciaAplicacion.setter
    def frecuenciaAplicacion(self, frecuenciaAplicacion):
        if frecuenciaAplicacion <= 0:
            raise ValueError("Error: la frecuencia de aplicación debe ser un valor positivo.")
        self.__frecuenciaAplicacion = frecuenciaAplicacion

    @property
    def precioProducto(self):
        return self.__precioProducto

    @precioProducto.setter
    def precioProducto(self, precioProducto):
        if precioProducto <= 0:
            raise ValueError("Error: el precio debe ser un valor positivo.")
        self.__precioProducto = precioProducto