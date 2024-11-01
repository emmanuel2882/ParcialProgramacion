from modelo.controlFertilizantes import ControlFertilizantes

class CRUDFertilizantes:
    #Almacen de 7 productos
    @staticmethod
    def create():
        fertilizante1 = ControlFertilizantes("Fertilizante1","ICA237",4,54000,"2024-02-14")
        fertilizante2 = ControlFertilizantes("Fertilizante2ca","ICA2968",4,134000,"2024-03-30")
        fertilizante3 = ControlFertilizantes("Fertilizante3white","ICA3457",9,340000,"2024-05-07")
        fertilizante4 = ControlFertilizantes("Fertilizante4light","ICA652",5,640000,"2024-03-15")
        fertilizante5 = ControlFertilizantes("Fertilizante5Sport","ICA960",8,1025000,"2024-01-12")
        fertilizante6 = ControlFertilizantes("Fertilizante6new","ICA941",4,120000,"2024-08-12")
        fertilizante7 = ControlFertilizantes("Fertilizante7PREMIUM","ICA225",8,1095000,"2024-09-12")
        

        return [fertilizante1,fertilizante2,fertilizante3,fertilizante4,fertilizante5,fertilizante6,fertilizante7] 