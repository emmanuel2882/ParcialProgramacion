from modelo.producto_plagas import ControlPlagas
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.antibioticos import Antibiotico

class UI:
    def mostrarMenuPrincipal(self):
        print("\n" + "=" * 80)
        print("\t\tMENÚ PRINCIPAL\n")
        print("1. Registrar nuevo cliente")
        print("2. Registrar nuevo producto")
        print("3. Consultar cliente")
        print("4. Eliminar cliente")
        print("5. Registrar venta de producto")
        print("=" * 80)
        opcion = int(input("Seleccione una opción: "))
        return opcion

    def interfazAgregarCliente(self):
        print("\n" + "=" * 80)
        print("\t\tINGRESO DE DATOS DEL CLIENTE\n")
        print("=" * 80)
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        return nombre, cedula

    def menuAgregarProductoControl(self):
        print("\n" + "=" * 80)
        print("\t\tMENÚ AGREGAR PRODUCTO\n")
        print("1. Producto de Control de Plagas")
        print("2. Fertilizante")
        print("3. Antibiótico")
        print("=" * 80)
        opcion = int(input("Seleccione una opción: "))
        return opcion

    def interfazAgregarProductoControl(self, opcionProducto):
        if opcionProducto == 1:
            nombre = input("Ingrese el nombre del producto de control de plagas: ")
            registroIca = input("Ingrese el registro ICA: ")
            frecuenciaAplicacion = int(input("Ingrese la frecuencia de aplicación: "))
            precioProducto = float(input("Ingrese el precio del producto: "))
            periodoCarencia = int(input("Ingrese el periodo de carencia: "))
            return ControlPlagas(nombre, registroIca, frecuenciaAplicacion, precioProducto, periodoCarencia)
        elif opcionProducto == 2:
            nombre = input("Ingrese el nombre del fertilizante: ")
            registroIca = input("Ingrese el registro ICA: ")
            frecuenciaAplicacion = int(input("Ingrese la frecuencia de aplicación: "))
            precioProducto = float(input("Ingrese el precio del producto: "))
            fechaUltimaAplicacion = input("Ingrese la fecha de última aplicación: ")
            return ControlFertilizantes(nombre, registroIca, frecuenciaAplicacion, precioProducto, fechaUltimaAplicacion)
        elif opcionProducto == 3:
            nombre = input("Ingrese el nombre del antibiótico: ")
            dosis = float(input("Ingrese la dosis: "))
            tipoAnimal = input("Ingrese el tipo de animal: ")
            precio = float(input("Ingrese el precio del antibiótico: "))
            return Antibiotico(nombre, dosis, tipoAnimal, precio)
        else:
            print("Opción no válida")
            return None

    def interfazBuscarCliente(self, crud):
        cedula = input("Ingrese la cédula del cliente a consultar: ")
        cliente = crud.buscar_por_cedula(cedula)
        if cliente:
            print(f"Cliente encontrado: {cliente}")
            for factura in cliente.facturas:
                print(f"Factura: {factura}")
                for producto in factura.productos_control:
                    print(f"Producto de Control: {producto}")
                for antibiotico in factura.antibioticos:
                    print(f"Antibiótico: {antibiotico}")
        else:
            print("Cliente no encontrado.")

    def interfazEliminarCliente(self):
        cedula = input("Ingrese la cédula del cliente a eliminar: ")
        return cedula

    def interfazVenderProducto(self):
        cedula = input("Ingrese la cédula del cliente para registrar la venta: ")
        return cedula