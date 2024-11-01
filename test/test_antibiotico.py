import unittest
from modelo.antibioticos import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def setUp(self):
        self.antibiotico = Antibiotico("Penicilina", 500, "bovinos", 150000)

    def test_creacion_correcta(self):
        self.assertEqual(self.antibiotico.nombreAntibiotico, "Penicilina")
        self.assertEqual(self.antibiotico.dosis, 500)
        self.assertEqual(self.antibiotico.tipoAnimal, "bovinos")
        self.assertEqual(self.antibiotico.precioAntibiotico, 150000)

    def test_nombre_invalido_vacio(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.nombreAntibiotico = ""
        self.assertEqual(str(context.exception), "Error: nombre de antibiótico vacío. Ingrese un nombre válido.")

    def test_nombre_invalido_caracteres(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.nombreAntibiotico = "Penicilin@123"
        self.assertEqual(str(context.exception), "Error: el nombre del antibiótico debe estar compuesto solo de espacios y letras.")

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.dosis = 100
        self.assertEqual(str(context.exception), "Error: dosis fuera del rango esperado. Por favor Ingrese un valor entre 400Kg y 600Kg.")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.precioAntibiotico = -100
        self.assertEqual(str(context.exception), "Error: el precio debe ser un valor positivo(>=0).")

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError) as context:
            self.antibiotico.tipoAnimal = "aves"
        self.assertEqual(str(context.exception), "Error: tipo de animal no válido.Solo tendras las siguientes opciones : 'bovinos', 'caprinos', 'porcinos'.")

if __name__ == "__main__":
    unittest.main()