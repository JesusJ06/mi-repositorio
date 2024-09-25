from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Formularios")

encabezado = Label(ventana, text="Formulario con Tkinter")
encabezado.config(
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#000000",
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W+E)

# Label para el campo (nombre)
label_nombre = Label(ventana, text="Nombre")
label_nombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de texto (nombre)
campo_texto_nombre = Entry(ventana)
campo_texto_nombre.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Label para el campo (apellidos)
label_apellidos = Label(ventana, text="Apellidos")
label_apellidos.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto_apellidos = Entry(ventana)
campo_texto_apellidos.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Label para el campo (descripcion)
label_descripcion = Label(ventana, text="Descripción")
label_descripcion.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Campo de texto grande (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campo_grande.config(width=30, height=5)

# Botón
# label(ventana).grid(row=4, column=1)
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10,bg="green",fg="white")




ventana.mainloop()


