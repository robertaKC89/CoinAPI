from models import CriptoModel
from views import CriptoView

class CriptoController: #controlador controla el flujo del programa y dice lo que hace usuario
    def __init__(self):   #aquí si pongo constructor porque el controlador necesita instancia, modelo y vista
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):    #me traigo 
        seguir = "S"
        while seguir == "S":
            desde, hasta = self.vista.pedir_monedas()   #1º. vista pide monedas a usuario

            #2º. paso a modelo las dos monedas con las que va a trabajar y luego que consulte cambio
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.consultar_cambio()

            self.vista.mostrar_cambio(desde, hasta, self.modelo.cambio) #3º. creado en vista, muestra cambio del modelo

            seguir = ""
            while seguir not in ("S", "N"):
                seguir = self.vista.quieres_seguir()
