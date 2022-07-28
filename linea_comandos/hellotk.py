# importo de módulo librería entero (me salto un poco las normas)
from tkinter import *
from tkinter import ttk

root = Tk()  # 1º.para crear la app necesito nodo de entrada e instancio Tk (aqui pinto las cosas)
marco = ttk.Frame (root, padding=50) #2º. defino recuadro que permite meterle cosas en lugar de meter en ventana principal
marco.grid ()   #3º.establezco posicionamiento, lo sitúo
# especificaré cosas que me hagan falta
etiqueta = Label(marco, text = 'hola TKinter',padx=50,pady=25, bg='white')  #defino
etiqueta.grid(row=0, column=0)  # sitúo

otra = Label(marco, text = 'soy otra etiqueta', fg='yellow',bg= '#333333',padx=100) #defino
otra.grid (row=5, column=0, columnspan=4)   #situo

vacia =Label(marco, text='',padx=50, pady=50)   #defino
vacia.grid (row=3, column=2)    #sitúo

uno = Button(marco, text='click me')    #defino
uno.grid (row=2, column=1)  #sitúo

# bucle principal que gestionará eventos y el programador ya no estará pendiente
root.mainloop()
