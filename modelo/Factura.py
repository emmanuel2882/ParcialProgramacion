class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.__antibioticos = []
        self.__productos_control = []
        self.__valor_total = 0

    @property
    def antibioticos(self):
        return self.__antibioticos
    
    @antibioticos.setter
    def antibioticos(self, antibiotico):
        self.__antibioticos.append(antibiotico)

    @property
    def productos_control(self):
        return self.__productos_control
    
    @productos_control.setter
    def productos_control(self, producto_control):
        self.__productos_control.append(producto_control)
        
    def asociar_antibiotico(self, antibiotico):
        self.__antibioticos.append(antibiotico)
        self.__valor_total += antibiotico.precioAntibiotico

    def asociar_producto_control(self, producto_control):
        self.__productos_control.append(producto_control)
        self.__valor_total += producto_control.precioProducto

    def realizarVenta(self, producto_control=None, antibiotico=None):
        if producto_control is not None:
            self.asociar_producto_control(producto_control)
        if antibiotico is not None:
            self.asociar_antibiotico(antibiotico)

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor):
        self.__valor_total = valor

    def __str__(self):
        return f"Factura(cliente={self.cliente.nombreCliente}, valor_total={self.valor_total})"