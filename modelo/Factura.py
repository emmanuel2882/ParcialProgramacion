from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        self.productos = []
        self.valor_total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.valor_total += producto.valor

    def __str__(self):
        productos_info = "\n".join([str(p) for p in self.productos])
        return (f"Factura para {self.cliente.nombre} (Cédula: {self.cliente.cedula})\n"
                f"Fecha: {self.fecha}\nProductos:\n{productos_info}\n"
                f"Valor Total: {self.valor_total}")