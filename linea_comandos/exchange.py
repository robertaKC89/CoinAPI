import requests 

apikey = 'AC10C799-7921-4EB0-BE3A-BBCB6C66F19F'  
cabeceras = {
    'X-CoinAPI-Key': apikey}  

seguir = 'S'    #inicializo el valor

while seguir.upper () == 'S':    # bucle por si el usuario quiere hacer más conversiones 
    # 1º. pido que se entre moneda origen y destino
    moneda_origen = input ('que moneda quieres cambiar?')
    moneda_destino = input ('que monedas deseas obtener?')

    #2º.junto api_url + endpoint y llamo para conversor de monedas
    url = f'http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}'

    #3º.hago la petición 
    respuesta=requests.get(url, headers = cabeceras)

    #4º.recibo json interpretable en python para convertir objeto en dicc. y poder acceder a datos de la web
    tipo_cambio = respuesta.json()

    #ej. un euro son xxxx bitcoins, un bitcoin son xxxx euros, un bitcoin son xxx dólares
    cambio = tipo_cambio ['rate']   #rate también lo saco de la web

    print('Un {} vale como {:,.2f} {}'.format(
        moneda_origen, cambio, moneda_destino)) #.format para tratar la info por separado mejor
    
    seguir = ''
    while seguir.upper () not in ('S', 'N'):
        seguir = input ('quieres hacer más cambios? S/N:')

