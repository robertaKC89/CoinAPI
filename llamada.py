import requests #lo 1º es importar de librería

apikey = 'AC10C799-7921-4EB0-BE3A-BBCB6C66F19F' # 2º. preparo mi apikey
cabeceras = {
    'X-CoinAPI-Key': apikey}   #3º. me genero diccionario cabeceras con codigo proporcionado + apikey

#4º. llamo a todos los datos que necesito: lo tengo en documentación CoinAPI.io en Market Dta - Rest API y en Metadata
api_url = 'http://rest.coinapi.io' #url base (hay que quitar barra última y tb he quitado sandobox de pruebas)
endpoint = '/v1/assets'  #ruta

url = api_url + endpoint    #5º. genero url definitiva a la que quiero llamar
respuesta = requests.get(url, headers=cabeceras)  #6º. hago petición get (librería) y luego me guardaré respuesta
codigo = respuesta.status_code  #7º. consulto qué código me devuelve de entre los existentes standard

if codigo ==200:    #8º. si el codigo a ido bien imprimo este resultado
    print ('las monedas disponibles son:')
    respuesta_json = respuesta.json ()  #recibo json interpretable en python para convertir objeto en dicc. y poder acceder a propiedades de la moneda
    for moneda in respuesta_json:   #para cada moneda en respuesta_json puedo acceder a pedir info. de web CoinAPI.io
        if moneda ['asset_id'].startswith('EUR'):
            print (moneda['asset_id'], moneda ['name'])

else:   #9º. si el codigo no ha ido bien imprimo este otro resultado 
    print ('la petición a la API ha fallado')
    print (f'codigo de error{codigo}')  #para que me imprima el codigo de la respuesta
    print (f'razón del error {respuesta.reason}')   #me da motivo que acompaña al codigo del error
    print (respuesta.text)  #vuelvo a imprimir para tener todos los datos
