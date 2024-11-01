from modelo.producto_plagas import ControlPlagas

class CRUDPlagas:
    #Almacen de 8 productos de control(plagas).
    @staticmethod
    def create():
        plaga1 = ControlPlagas("Plaga1","ICA2376",4,54000,15)
        plaga2 = ControlPlagas("Plaga2red","ICA296",4,134000,15)
        plaga3 = ControlPlagas("Plaga3BLACH","ICA345",9,340000,30)
        plaga4 = ControlPlagas("Plaga4WHITE","ICA789",5,540000,30)
        plaga5 = ControlPlagas("Plaga5Yellow","ICA992",8,925000,90)
        plaga6 = ControlPlagas("Plaga6new","ICA255",4,54000,15)
        plaga7 = ControlPlagas("Plaga7road","ICA663",4,134000,15)
        plaga8 = ControlPlagas("Plaga8blue","ICA888",9,340000,30)

        return [plaga1,plaga2,plaga3,plaga4,plaga5,plaga6,plaga7,plaga8]