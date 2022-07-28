# importo de módulo librería entero (me salto un poco las normas)
from tkinter import *
from tkinter import ttk

root = Tk()  # para crear la app necesito nodo de entrada e instancio Tk
# especificaré cosas que me hagan falta
etiqueta = Label(root, 'text = hola TKinter')
etiqueta.pack()  # con el pack la hago visible en ventana

otra = Label(root, 'text = soy otra etiqueta')
# bucle principal que gestionará eventos y el programador ya no estará pendiente
root.mainloop()
