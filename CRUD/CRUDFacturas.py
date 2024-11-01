from CRUD.CRUDAntibiotico import CRUDAntibiotico
from CRUD.CRUDFertilizante import CRUDFertilizantes
from CRUD.CRUDPlagas import CRUDPlagas
from modelo.factura import Factura

class CrudFacturas:
    @staticmethod
    def crearFacturas():
        plagasDisponibles = CRUDPlagas()
        fertilizantesDisponibles = CRUDFertilizantes()
        antibioticosDisponibles = CRUDAntibiotico()
        inventarioPlagas = plagasDisponibles.create()
        inventarioFertilizantes = fertilizantesDisponibles.create()
        inventarioAntibioticos = antibioticosDisponibles.create()
        # Se crean 5 facturas y se asocian con productos y antibióticos.
        factura1 = Factura()
        factura1.asociar_antibiotico(inventarioAntibioticos[0])
        factura1.asociar_producto_control(inventarioPlagas[0])
        factura1.asociar_producto_control(inventarioFertilizantes[0])
        factura2 = Factura()
        factura2.asociar_antibiotico(inventarioAntibioticos[0])
        factura2.asociar_producto_control(inventarioPlagas[1])
        factura2.asociar_producto_control(inventarioFertilizantes[2])
        factura3 = Factura()
        factura3.asociar_antibiotico(inventarioAntibioticos[4])
        factura3.asociar_producto_control(inventarioPlagas[3])
        factura3.asociar_producto_control(inventarioFertilizantes[1])
        factura4 = Factura()
        factura4.asociar_antibiotico(inventarioAntibioticos[4])
        factura4.asociar_antibiotico(inventarioAntibioticos[3])
        factura4.asociar_producto_control(inventarioPlagas[3])
        factura4.asociar_producto_control(inventarioFertilizantes[3])
        factura5 = Factura()
        factura5.asociar_producto_control(inventarioPlagas[4])
        factura6 = Factura()
        factura6.asociar_antibiotico(inventarioAntibioticos[0])
        factura6.asociar_producto_control(inventarioPlagas[1])
        factura6.asociar_producto_control(inventarioFertilizantes[2])
        factura7 = Factura()
        factura7.asociar_antibiotico(inventarioAntibioticos[4])
        factura7.asociar_producto_control(inventarioPlagas[3])
        factura7.asociar_producto_control(inventarioFertilizantes[1])
        
        return [factura1, factura2, factura3, factura4, factura5, factura6, factura7]