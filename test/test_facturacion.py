import unittest
from modelo.Cliente import Cliente
from modelo.Factura import Factura
from modelo.ControlDeFertilizantes import ControlDeFertilizantes
from modelo.Antibiotico import Antibiotico

class TestSistemaFacturacion(unittest.TestCase):

    # Escenario 1: Crear una factura con productos y verificar valor total
    def test_crear_factura_con_productos(self):
        cliente = Cliente("Juan Pérez", "123456789")
        fertilizante = ControlDeFertilizantes("Fertilizante A", 15000, "12345", "30 días", "2024-01-15")
        antibiotico = Antibiotico("Antibiótico B", 10000, "500kg", "Bovino")

        factura = Factura(cliente)
        factura.agregar_producto(fertilizante)
        factura.agregar_producto(antibiotico)

        # Verificar valor total
        self.assertEqual(factura.valor_total, 25000)
        # Verificar cantidad de productos
        self.assertEqual(len(factura.productos), 2)

    # Escenario 2: Crear una factura sin productos y verificar que el valor total sea 0
    def test_factura_sin_productos(self):
        cliente = Cliente("María López", "987654321")
        factura = Factura(cliente)

        # Verificar que el valor total es 0
        self.assertEqual(factura.valor_total, 0)
        # Verificar que no hay productos
        self.assertEqual(len(factura.productos), 0)

    # Escenario 3: Verificar que los atributos obligatorios de los productos se asignen correctamente
    def test_asignacion_atributos_productos(self):
        fertilizante = ControlDeFertilizantes("Fertilizante C", 20000, "54321", "15 días", "2024-05-20")
        antibiotico = Antibiotico("Antibiótico D", 12000, "600kg", "Porcino")

        # Verificar que los atributos se asignen correctamente
        self.assertEqual(fertilizante.nombre, "Fertilizante C")
        self.assertEqual(fertilizante.valor, 20000)
        self.assertEqual(fertilizante.registro_ica, "54321")
        self.assertEqual(fertilizante.frecuencia_aplicacion, "15 días")
        self.assertEqual(fertilizante.fecha_ultima_aplicacion, "2024-05-20")

        self.assertEqual(antibiotico.nombre, "Antibiótico D")
        self.assertEqual(antibiotico.valor, 12000)
        self.assertEqual(antibiotico.dosis, "600kg")
        self.assertEqual(antibiotico.tipo_animal, "Porcino")

    # Escenario 4: Probar el comportamiento cuando se agregan varios productos del mismo tipo
    def test_factura_con_varios_productos_mismo_tipo(self):
        cliente = Cliente("Luis García", "555666777")
        fertilizante1 = ControlDeFertilizantes("Fertilizante A", 18000, "11111", "30 días", "2024-03-01")
        fertilizante2 = ControlDeFertilizantes("Fertilizante B", 22000, "22222", "45 días", "2024-04-10")

        factura = Factura(cliente)
        factura.agregar_producto(fertilizante1)
        factura.agregar_producto(fertilizante2)

        # Verificar valor total de los productos agregados
        self.assertEqual(factura.valor_total, 40000)
        # Verificar que hay 2 productos en la factura
        self.assertEqual(len(factura.productos), 2)

if __name__ == '__main__':
    unittest.main()
