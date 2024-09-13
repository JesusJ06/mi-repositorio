from tkinter import*

ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(0,0)

texto = Label(ventana, text="bienvenido a mi programa")

texto.config(
        fg="white",
        bg="#000000",
        padx=50,
        pady=20,
        font=("Arial",30)
)
texto.pack() 


texto= Label(ventana, text="soy victor robles")
texto.config(
    
    height=2,
    bg="orange",
    font=("Arial",18),
    padx=18,
    pady=20,
    cursor=("circle",)

   
)
texto.pack(anchor=E) 


def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido} veo que eres de {pais}"

texto = Label(ventana, text= pruebas(nombre="jesus", apellido="jimenez", pais="españa"))
texto.config(
    height=2,
    bg="green",
    font=("Arial",14),
    padx=10,
    pady=10
)
texto.pack(anchor=W) 
ventana.mainloop()