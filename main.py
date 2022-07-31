# archivo para instanciar CriptoController y arrancar el llop principal:
from cripto_cambio.controllers import CriptoControllerTk

#lanzo para que funcione solo cuando lo hago desde linea_comandos
if __name__ == '__main__':
    app = CriptoControllerTk()  #me instancio mi app que controla todo el proceso
    app.run ()  #llamo al método  
    