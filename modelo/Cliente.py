class Cliente:
    def __init__(self, nombreCliente: str, cedula: str):
        self.__nombreCliente = nombreCliente  
        self.__cedula = cedula                  
        self.__facturas = []                    

    # Propiedad nombreCliente con su validación
    @property
    def nombreCliente(self):
        return self.__nombreCliente

    @nombreCliente.setter
    def nombreCliente(self, nombreCliente):
        if len(nombreCliente) >= 3:
            self.__nombreCliente = nombreCliente
        else:
            raise ValueError("Error: el nombre debe tener mínimo 3 caracteres.")

    # Propiedad cedula con su validación
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        if cedula.isdigit() and len(cedula) >= 7:
            self.__cedula = cedula
        else:
            raise ValueError("Error: la cédula debe ser numérica y tener mínimo 7 dígitos.")
    
    # Propiedad facturas para agregar facturas al cliente
    @property
    def facturas(self):
        return self.__facturas
    
    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)

    def __str__(self):
        return f"Cliente(nombre={self.__nombreCliente}, cedula={self.__cedula})"