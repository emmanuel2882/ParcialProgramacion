import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CRUD.CRUDutilidades import CRUD
from CRUD.CRUDCliente import CRUDCLiente
from CRUD.CRUDFacturas import CrudFacturas

Base_de_datos = CRUD()
facturas = CrudFacturas()
clientes = CRUDCLiente()

lista_facturas_creadas = facturas.crearFacturas()
lista_clientes_creados = clientes.create()

# Asociar clientes a la base de datos
for cliente in lista_clientes_creados:
    Base_de_datos.agregar_cliente(cliente)

# asociar facturas a clientes de la base de datos Factura[0] se asocia a Cliente[0] solo para la prueba
for i, cliente in enumerate(lista_clientes_creados):
    Base_de_datos.asociar_factura(cliente, [lista_facturas_creadas[i]])


