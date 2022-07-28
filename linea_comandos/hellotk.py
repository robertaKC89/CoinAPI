from tkinter import * # importo de módulo librería entero (me salto un poco las normas)
from tkinter import ttk

root = Tk ()    #para crear la app necesito nodo de entrada e instancio Tk
etiqueta = Label (root, 'text = hola TKinter') #especificaré cosas que me hagan falta 
etiqueta.pack () #con el pack la hago visible en ventana

otra = Label (root, 'text = soy otra etiqueta')
root.mainloop ()    #bucle principal que gestionará eventos y el programador ya no estará pendiente 

