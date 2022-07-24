"""

 Modelo <=> Controlador <=> Vista

 Modelo </////> Vista   (NUNCA hay comunicación entre el modelo y la vista directamente)

"""

class CriptoView:   #vista hace 2 cosas: pide cambio monedas y muestra resultados (no almacena datos)

    def pedir_monedas(self):  # me he traído los inputs/entrada usuario
        origen = input("¿Qué moneda quieres cambiar? ") 
        destino = input("¿Qué moneda deseas obtener? ")
        return (origen, destino)    #lo comunica al controlador para que lo pase al modelo!!! 

    def mostrar_cambio(self, origen, destino, cambio):  #me he traído el print/salida usuario
        print("Un {} vale como {:,.2f} {}".format(origen, cambio, destino,))
