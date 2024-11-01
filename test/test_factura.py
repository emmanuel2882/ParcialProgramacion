import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modelo.factura import Factura as factura
from modelo.antibioticos import Antibiotico as antibiotico
from modelo.controlFertilizantes import ControlFertilizantes as producto_fertilizante
from modelo.producto_plagas import ControlPlagas as producto_plaga
from modelo.productosDeControl import ProductoControl as pc
from modelo.cliente import Cliente as cliente

class TestFactura(unittest.TestCase):
    def setUp(self):
        self.cliente = cliente("emmanuel", "12345678")
        self.pc_plaga = producto_plaga("Plaga", "ICA124", 8, 20000, 20)
        self.pc_fertilizante = producto_fertilizante("fertilizante", "ICA7028", 15, 60000, 10)
        self.fact = factura(self.cliente)

    def test_vende_varios_producto_control(self):
        self.fact.asociar_producto_control(self.pc_plaga)
        self.fact.asociar_producto_control(self.pc_fertilizante)

        self.assertEqual(2, len(self.fact.productos_control), "No se ha asociado producto control")

    def test_vende_varios_antibioticos(self):
        ant_1 = antibiotico("anti_1", 10, "bovino", 120000)
        ant_2 = antibiotico("anti_2", 8, "caprino", 100000)
        self.fact.asociar_antibiotico(ant_1)
        self.fact.asociar_antibiotico(ant_2)

        self.assertEqual(2, len(self.fact.antibioticos), "No se ha asociado antibiotico")

    def test_vende_varios_producto_control_antibioticos(self):
        ant_1 = antibiotico("anti_1", 10, "bovino", 120000)
        ant_2 = antibiotico("anti_2", 8, "caprino", 100000)
        pc_plaga = producto_plaga("Plaga X", "ICA124", 8, 20000, 20)
        pc_fertilizante = producto_fertilizante("ferilizante", "ICA7028", 15, 60000, 10)

        self.fact.asociar_producto_control(pc_plaga)
        self.fact.asociar_producto_control(pc_fertilizante)
        self.fact.asociar_antibiotico(ant_1)
        self.fact.asociar_antibiotico(ant_2)

        self.assertEqual(2, len(self.fact.antibioticos), "No se ha asociado antibiotico")
        self.assertEqual(2, len(self.fact.productos_control), "No se ha asociado producto control")

if __name__ == "__main__":
    unittest.main()
