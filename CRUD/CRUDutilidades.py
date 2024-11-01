from modelo.cliente import Cliente
from modelo.factura import Factura

class CRUD:
    def __init__(self):
        self.clientes = []  # Inicializa la lista de clientes en el sistema

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente agregado: {cliente}")  # Añade un print para verificar que el cliente se agrega

    def buscar_por_cedula(self, cedula):
        for cliente in self.clientes:
            print(f"Buscando en cliente: {cliente.cedula}")
            if cliente.cedula == cedula:
                return cliente
        return None

    def eliminar_cliente(self, cedula):
        cliente = self.buscar_por_cedula(cedula)
        if cliente is None:
            raise ValueError("No se puede eliminar, el cliente no existe.")
        self.clientes.remove(cliente)

    def asociar_factura(self, cliente, facturas):
        if cliente not in self.clientes:
            raise ValueError("El cliente no existe.")
        cliente.facturas.extend(facturas)