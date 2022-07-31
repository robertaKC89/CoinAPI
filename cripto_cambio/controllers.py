from tkinter import Tk
from models import CriptoModel
from views import CriptoView, CriptoViewTk

class CriptoController: #controlador controla el flujo del programa y dice lo que hace usuario
    def __init__(self):   #aquí si pongo constructor porque el controlador necesita instanciar modelo y vista
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

class CriptoControllerTk(Tk):   #Tk es la raíz, debe pintarse aquí! Controla que la app arranque, tenga en mainloop y se cierre!
    def __init__(self):
        super().__init__()
        self.vista = CriptoViewTk(self, self.calcular_cambio)
        self.modelo = CriptoModel()

    def run(self):  # función bucle principal para llamar al mainloop
        self.mainloop() #llamo

    def calcular_cambio(self):
        """
        Recoge los datos de la vista
        los pasa al modelo
        pide el cambio al modelo
        le pasa el resultado del cambio a la vista
        """
        self.modelo.moneda_origen = self.vista.moneda_origen()
        self.modelo.moneda_destino = self.vista.moneda_destino()
        self.modelo.consultar_cambio()

        self.vista.mostrar_cambio(self.modelo.cambio)
