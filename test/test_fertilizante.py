import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modelo.controlFertilizantes import ControlFertilizantes

class TestFertilizante(unittest.TestCase):

    def setUp(self):
        self.fertilizante = ControlFertilizantes("FertiGrow", "ICA123", 30, 100000, "2024-10-01")

    def test_creacion_correcta(self):
        self.assertEqual(self.fertilizante.nombreProducto, "FertiGrow")
        self.assertEqual(self.fertilizante.registroIca, "ICA123")
        self.assertEqual(self.fertilizante.frecuenciaAplicacion, 30)
        self.assertEqual(self.fertilizante.precioProducto, 100000)
        self.assertEqual(self.fertilizante.fechaUltimaAplicacion, "2024-10-01")

    def test_registro_ica_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.registroIca = ""
        self.assertEqual(str(context.exception), "Error: registro ICA vacío. Ingrese un registro válido.")

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.nombreProducto = ""
        self.assertEqual(str(context.exception), "Error: nombre del producto vacío. Ingrese un nombre válido.")

    def test_frecuencia_aplicacion_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.frecuenciaAplicacion = -10
        self.assertEqual(str(context.exception), "Error: la frecuencia de aplicación debe ser un valor positivo.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.precioProducto = -1000
        self.assertEqual(str(context.exception), "Error: el precio debe ser un valor positivo.")

    def test_fecha_ultima_aplicacion_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.fertilizante.fechaUltimaAplicacion = ""
        self.assertEqual(str(context.exception), "Error: la fecha de última aplicación es obligatoria. Ingrese un valor válido.")

if __name__ == "__main__":
    unittest.main()