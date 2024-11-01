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
from CRUD.CRUDutilidades import CRUD

class TestCRUD(unittest.TestCase):
    def setUp(self):
        self.crud = CRUD() 
        self.cliente_1 = cliente("Emmanuel Henao", "12345678")
        self.cliente_2 = cliente("Isabella Henao", "87654321")

        self.factura_1 = factura(self.cliente_1)
        self.factura_2 = factura(self.cliente_2)
        
        self.pc_plaga = producto_plaga("Plaga", "ICA124", 8, 20000, 20)
        self.pc_fertilizante = producto_fertilizante("Fertilizante", "ICA7028", 15, 120000, 10)
       
        self.antibiotico_1 = antibiotico("anti_1", 10, "bovino", 120000)
        self.antibiotico_2 = antibiotico("anti_2", 8, "caprino", 100000)

    def test_agregar_cliente(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.agregar_cliente(self.cliente_2)
        self.assertEqual(len(self.crud.clientes), 2, "No se agregaron los clientes correctamente.")

    def test_buscar_por_cedula(self):
        self.crud.agregar_cliente(self.cliente_1)
        cliente_encontrado = self.crud.buscar_por_cedula("12345678")
        self.assertIsNotNone(cliente_encontrado, "El cliente no fue encontrado.")
        self.assertEqual(cliente_encontrado.nombreCliente, "Emmanuel", "El nombre del cliente no coincide.")

    def test_eliminar_cliente(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.eliminar_cliente("12345678")
        cliente_eliminado = self.crud.buscar_por_cedula("12345678")
        self.assertIsNone(cliente_eliminado, "El cliente no fue eliminado correctamente.")

    def test_eliminar_cliente_inexistente(self):
        with self.assertRaises(ValueError, msg="No se generó la excepción adecuada al intentar eliminar un cliente inexistente."):
            self.crud.eliminar_cliente("99999999")

    def test_buscar_cliente_inexistente(self):
        cliente_no_encontrado = self.crud.buscar_por_cedula("99999999")
        self.assertIsNone(cliente_no_encontrado, "No se manejó correctamente la búsqueda de un cliente inexistente.")

    def test_asociar_factura(self):
        self.crud.agregar_cliente(self.cliente_1)
        self.crud.asociar_factura(self.cliente_1, [self.factura_1, self.factura_2])
        self.assertEqual(len(self.cliente_1.facturas), 2, "Las facturas no fueron asociadas correctamente al cliente.")

    def test_asociar_factura_cliente_inexistente(self):
        cliente_falso = cliente("Falso Cliente", "00000000")
        with self.assertRaises(ValueError, msg="No se generó la excepción adecuada al intentar asociar facturas a un cliente inexistente."):
            self.crud.asociar_factura(cliente_falso, [self.factura_1])

if __name__ == "__main__":
    unittest.main()
