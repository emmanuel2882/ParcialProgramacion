import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modelo.producto_plagas import ControlPlagas

class TestPlaga(unittest.TestCase):

    def setUp(self):
        self.plaga = ControlPlagas("insecticida", "ICA789", 15, 80000, 7)

    def test_creacion_correcta(self):
        self.assertEqual(self.plaga.nombreProducto, "insecticida")
        self.assertEqual(self.plaga.registroIca, "ICA789")
        self.assertEqual(self.plaga.frecuenciaAplicacion, 15)
        self.assertEqual(self.plaga.precioProducto, 80000)
        self.assertEqual(self.plaga.periodoCarencia, 7)

    def test_periodo_carencia_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.periodoCarencia = -5
        self.assertEqual(str(context.exception), "Error: el periodo de carencia debe ser mayor que cero. Por favor ingrese un valor positivo.")

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.nombreProducto = ""
        self.assertEqual(str(context.exception), "Error: nombre del producto vacío. Ingrese un nombre válido.")

    def test_registro_ica_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.registroIca = ""
        self.assertEqual(str(context.exception), "Error: registro ICA vacío. Ingrese un registro válido.")

    def test_frecuencia_aplicacion_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.frecuenciaAplicacion = -10
        self.assertEqual(str(context.exception), "Error: la frecuencia de aplicación debe ser un valor positivo.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.plaga.precioProducto = -1000
        self.assertEqual(str(context.exception), "Error: el precio debe ser un valor positivo.")

if __name__ == "__main__":
    unittest.main()
