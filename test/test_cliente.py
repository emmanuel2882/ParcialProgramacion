import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo.factura import Factura as factura
from modelo.antibioticos import Antibiotico as antibiotico
from modelo.controlFertilizantes import ControlFertilizantes as producto_fertilizante
from modelo.producto_plagas import ControlPlagas as producto_plaga
from modelo.cliente import Cliente as cliente

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = cliente("santiago gonzales", "10243580")
        self.factura_1 = factura(self.cliente)
        self.factura_2 = factura(self.cliente)

        self.antibiotico_1 = antibiotico("anti_1", 10, "bovino", 120000)
        self.antibiotico_2 = antibiotico("anti_2", 8, "caprino", 100000)
        self.pc_plaga = producto_plaga("Plaga X", "ICA124", 8, 20000, 20)
        self.pc_fertilizante = producto_fertilizante("UREA", "ICA7028", 15, 60000, 10)

    def test_cliente_tiene_varias_facturas_asociadas(self):
        self.factura_1.asociar_antibiotico(self.antibiotico_1)
        self.factura_1.asociar_antibiotico(self.antibiotico_2)
        self.factura_1.asociar_producto_control(self.pc_plaga)
        self.factura_1.asociar_producto_control(self.pc_fertilizante)

        self.factura_2.asociar_antibiotico(self.antibiotico_1)
        self.factura_2.asociar_antibiotico(self.antibiotico_2)
        self.factura_2.asociar_producto_control(self.pc_plaga)
        self.factura_2.asociar_producto_control(self.pc_fertilizante)

        self.cliente.facturas = self.factura_1
        self.cliente.facturas = self.factura_2

        self.assertEqual(2, len(self.cliente.facturas), "Cliente no tiene facturas asociadas")

if __name__ == "__main__":
    unittest.main()