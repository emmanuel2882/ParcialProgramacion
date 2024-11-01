from modelo.cliente import Cliente

class CRUDCLiente:
    @staticmethod
    def create():
        cliente1 = Cliente("Emmanuel Henao Guarin","123456789")
        cliente2 = Cliente("Isabella Henao", "456789123")
        cliente3 = Cliente("Stella Ortiz","564238974")
        cliente4 = Cliente("Juan Jose Hernandez","203516894")
        cliente5 = Cliente("Angie Carolina Rivera","623148509")
        cliente6 = Cliente("Franciso Javier","245516894")
        cliente7 = Cliente("Ana Paula Oliveros","623156309")

        return [cliente1,cliente2,cliente3,cliente4,cliente5,cliente6,cliente7]
