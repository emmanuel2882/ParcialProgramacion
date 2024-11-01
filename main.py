from modelo.cliente import Cliente
from modelo.antibioticos import Antibiotico
from modelo.controlFertilizantes import ControlFertilizantes
from modelo.producto_plagas import ControlPlagas
from modelo.factura import Factura
from CRUD.CRUDutilidades import CRUD
from ui.ui import UI

def main():
    # Se instancian las clases
    crud = CRUD()
    ui = UI()
    
    while True:
        opcion = ui.mostrarMenuPrincipal()  # Mostrar el menú principal y obtener la opción del usuario

        # Manejar las diferentes opciones
        if opcion == 1:
            # Lógica para registrar un nuevo cliente
            nombre, cedula = ui.interfazAgregarCliente()
            nuevo_cliente = Cliente(nombre, cedula)
            crud.agregar_cliente(nuevo_cliente)
            print("Cliente registrado exitosamente.")
        elif opcion == 2:
            # Lógica para registrar un nuevo producto
            opcionProducto = ui.menuAgregarProductoControl()
            producto = ui.interfazAgregarProductoControl(opcionProducto)
            print(f"Producto registrado exitosamente: {producto}")
        elif opcion == 3:
            # Lógica para consultar un cliente y mostrar sus facturas
            ui.interfazBuscarCliente(crud)
        elif opcion == 4:
            # Lógica para eliminar un cliente
            cedula = ui.interfazEliminarCliente()
            try:
                crud.eliminar_cliente(cedula)
                print("Cliente eliminado exitosamente.")
            except ValueError as e:
                print(e)
        elif opcion == 5:
            # Lógica para registrar venta de producto
            cedula = ui.interfazVenderProducto()
            cliente = crud.buscar_por_cedula(cedula)
            if cliente:
                opcionProducto = ui.menuAgregarProductoControl()
                producto = ui.interfazAgregarProductoControl(opcionProducto)
                if producto:
                    factura = Factura(cliente)
                    if isinstance(producto, ControlPlagas) or isinstance(producto, ControlFertilizantes):
                        factura.asociar_producto_control(producto)
                    elif isinstance(producto, Antibiotico):
                        factura.asociar_antibiotico(producto)
                    crud.asociar_factura(cliente, [factura])
                    print(f"Venta registrada para el cliente: {cliente.nombreCliente}")
            else:
                print("Cliente no encontrado.")
        else:
            print("Opción no válida")

        # Preguntar al usuario si desea realizar otra operación
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()