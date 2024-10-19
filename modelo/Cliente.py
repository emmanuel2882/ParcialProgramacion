class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.historial_facturas = []

    def agregar_factura(self, factura):
        self.historial_facturas.append(factura)

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"
