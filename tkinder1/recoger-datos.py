from tkinter import *

ventana = Tk()
ventana.geometry("700x700")

ventana.config(
    bd=50,
    bg="#ccc"
)
dato = ""
Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
Label(ventana, text=dato).pack(anchor=NW)

Button()

ventana.mainloop()