from modelo.Producto  import Producto
class Antibiotico(Producto):
    def __init__(self, nombre, valor, dosis, tipo_animal):
        super().__init__(nombre, valor)
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    def __str__(self):
        return (f"{super().__str__()}, Dosis: {self.dosis}kg, "
                f"Tipo de Animal: {self.tipo_animal}")
