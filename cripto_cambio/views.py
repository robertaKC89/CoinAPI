from tkinter import StringVar, ttk
from . import MONEDAS
"""
 Modelo <=> Controlador <=> Vista

 Modelo </////> Vista   (NUNCA hay comunicación entre el modelo y la vista directamente)

"""

class CriptoView:   #vista hace 2 cosas: pide cambio monedas y muestra resultados (no almacena datos, interactúa con user)

    def pedir_monedas(self):  # me he traído los inputs/entrada usuario
        origen = input("¿Qué moneda quieres cambiar? ") 
        destino = input("¿Qué moneda deseas obtener? ")
        return (origen, destino)    #lo comunica al controlador para que lo pase al modelo!!! 

    def mostrar_cambio(self, origen, destino, cambio):  #me he traído el print/salida usuario
        print("Un {} vale como {:,.2f} {}".format(origen, cambio, destino,))

    def quieres_seguir(self):
        seguir = input("¿Quieres cambiar algo más? (s/n) ")
        return seguir.upper()

class CriptoViewTk(ttk.Frame):  #genero mi vista como un Frame para aprovechar todo lo que tenga el Frame
    def __init__ (self, padre):
        super().__init__(padre, width=400, height=400, padding=20)  #llamo al padre donde me voy a pintar como Frame
        self.grid ()    #llamo al frame y le digo que es de tipo grid
        self.crear_controles()

    def crear_controles(self):
        ejemplo = ttk.Label(self, text="Criptocambio")  #etiqueta se pinta en el marquito, no en ventana principal 
        ejemplo.grid(row=0, column=0)   #para dar posicionamiento cuadrícula a la etiqueta 

        # entrada moneda origen
        etiqueta_entrada = ttk.Label(self, text="Moneda origen")
        etiqueta_entrada.grid(row=0, column=0)  #pinto

        self.origen = StringVar()   # guardo variable y uso campo para pasarla al controlador ya que recojo strings
        # a cada combobox le paso: dónde se pinta + valores que enseñará + variable con la que quiero vincular
        combo_entrada = ttk.Combobox(self, values=MONEDAS, textvariable=self.origen) 
        combo_entrada.grid(row=1, column=0) #pinto

        # entrada moneda destino
        etiqueta_destino = ttk.Label(self, text="Moneda destino")
        etiqueta_destino.grid(row=0, column=1)  #pinto

        self.destino = StringVar ()
        combo_destino = ttk.Combobox(self, values=MONEDAS, textvariable=self.destino)   #Combobox crea desplegable
        combo_destino.grid(row=1, column=1) #pinto

        # etiqueta para el resultado
        self.etiqueta_resultado = ttk.Label(self, text="0.0", padding=20)
        self.etiqueta_resultado.grid(row=2, column=0, columnspan=2) #que se expanda en las 2 columnas

        # botón para el cambio
        # funcion especifica de botones es command al que le debo pasar función que quiero ejecutar!
        self.boton_calcular = ttk.Button(self, text="Calcular", command=self.lo_que_hace_el_boton)
        self.boton_calcular.grid(row=3, column=1)
    
    # llamo para devolver lo del campo StringVar (consultar apuntes)
    def moneda_origen(self):
        return self.origen.get()[:3]    # aqui solo quiero que me coja 3 primeros caracteres
    def moneda_destino(self):
        return self.destino.get()[:3]

    def lo_que_hace_el_boton(self): # no lo ejecuto, paso la función al botón para cuando se ejecute
        #llamo a los métodos anteriores que ya llevan el .get para pasar al modelo a través del controlador
        print("La moneda origen es", self.moneda_origen())  
        print("La moneda destino es", self.moneda_destino())


