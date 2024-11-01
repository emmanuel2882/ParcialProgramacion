class Antibiotico:
    def __init__(self, nombreAntibiotico: str, dosis: float, tipoAnimal: str, precioAntibiotico: float):
        self.__nombreAntibiotico = nombreAntibiotico  
        self.__dosis = dosis  
        self.__tipoAnimal = tipoAnimal  
        self.__precioAntibiotico = precioAntibiotico  

    # Propiedad nombreAntibiotico con su validación
    @property
    def nombreAntibiotico(self):
        return self.__nombreAntibiotico

    @nombreAntibiotico.setter
    def nombreAntibiotico(self, nombreAntibiotico):
        if not nombreAntibiotico.strip():
            raise ValueError("Error: nombre de antibiótico vacío. Ingrese un nombre válido.")
        if not all(char.isalpha() or char.isspace() for char in nombreAntibiotico):
            raise ValueError("Error: el nombre del antibiótico debe estar compuesto solo de espacios y letras.")
        self.__nombreAntibiotico = nombreAntibiotico

    # Propiedad dosis con su validación
    @property
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
        if 400 <= dosis <= 600:
            self.__dosis = dosis
        else:
            raise ValueError("Error: dosis fuera del rango esperado. Por favor Ingrese un valor entre 400Kg y 600Kg.")

    # Propiedad tipoAnimal con su validación
    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        if tipoAnimal.lower() in ['bovinos', 'caprinos', 'porcinos']:
            self.__tipoAnimal = tipoAnimal
        else:
            raise ValueError("Error: tipo de animal no válido.Solo tendras las siguientes opciones : 'bovinos', 'caprinos', 'porcinos'.")

    # Propiedad precioAntibiotico con su validación
    @property
    def precioAntibiotico(self):
        return self.__precioAntibiotico

    @precioAntibiotico.setter
    def precioAntibiotico(self, precioAntibiotico):
        if precioAntibiotico <= 0:
            raise ValueError("Error: el precio debe ser un valor positivo(>=0).")
        self.__precioAntibiotico = precioAntibiotico
    def __str__(self):
        return f"Antibiotico(nombreAntibiotico={self.nombreAntibiotico}, dosis={self.dosis}, tipoAnimal={self.tipoAnimal}, precioAntibiotico={self.precioAntibiotico})"