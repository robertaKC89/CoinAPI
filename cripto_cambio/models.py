import requests #es librería de terceros, por ello importo antes que la mía
from . import APIKEY

class APIError(Exception):  #hereda de exception que es de Python
    pass


class CriptoModel:  # quiero hacer un modelo que mantenga los datos y haga las llamadas a la API
    """
    - moneda origen
    - moneda destino
    - dato del cambio
    - consultar cambio (método)
    """

    def __init__(self, origen, destino):    #manera en que le llegan los datos al modelo de parte del controlador
        """
        Construye un objeto con las monedas origen y destino
        y el cambio obtenido desde CoinAPI inicializado a cero.
        """
        self.moneda_origen = origen #ya no es variable local sino atributo de la class
        self.moneda_destino = destino  # ya no es variable local sino atributo de la class
        self.cambio = 0.0

    def consultar_cambio(self): # creo este método y me traigo cosas de exchange!
        """
        Consulta el cambio entre la moneda origen y la moneda destino
        utilizando la API REST CoinAPI.
        """
        cabeceras = {"X-CoinAPI-Key": APIKEY}
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=cabeceras)

        if respuesta.status_code == 200:    #con status_code compruebo si la respuesta ha ido bien
            self.cambio = respuesta.json()["rate"]  # si ha ido bien guardo el cambio obtenido
        else:
            raise APIError("Ha ocurrido un error {} {} al consultar la API.".format(
                respuesta.status_code, respuesta.reason))   #error generado por API que defino en class y le pido todos los detalles


