class Producto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f"Producto: {self.nombre}, Valor: {self.valor}"
