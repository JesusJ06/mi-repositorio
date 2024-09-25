from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("500x500")

Label(ventana,text="hola").pack()

imagen = Image.open('123.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()