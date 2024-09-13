from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("500x500")

# texto = Label(ventana, text="Bienvenido a mi programa")

# texto.config(
#         fg="blue",
#         bg="black",
#         padx=100,
#         pady=20,
#         font=("Arial", 18)
# )
# texto.pack()

# texto = Label(ventana, text="Hola")
# texto.config(
#     fg="red",
#     bg="yellow",
#     padx=100,
#     pady=20,
#     font=("Arial", 20),
#     cursor="circle"
# )

# cargar imagen
Label(ventana,text="hola").pack(anchor=W)

imagen = Image.open("123.jpg")
render = ImageTk.PhotoImagen(imagen)

Label(ventana, image=render).pack()

ventana.mainloop() 