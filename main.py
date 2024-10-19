from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.ControlDeFertilizantes import ControlDeFertilizantes
from modelo.Antibiotico import Antibiotico

def main():
    # Crear un cliente
    cliente = Cliente("Emmanuel Henao", "123456789")

    # Crear algunos productos
    fertilizante = ControlDeFertilizantes("Fertilizante A", 15000, "12345", "30 días", "2024-01-15")
    antibiotico = Antibiotico("Antibiótico B", 10000, "500kg", "Bovino")

    # Crear una factura y agregar productos
    factura = Factura(cliente)
    factura.agregar_producto(fertilizante)
    factura.agregar_producto(antibiotico)

    # Mostrar la factura
    print(factura)

if __name__ == "__main__":
    main()
