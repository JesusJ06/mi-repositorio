from tkinter import *
from tkinter import messagebox as MessageBox
ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
        MessageBox.showinfo("Alerta","Hola soy Jesus")

Button(ventana,text="Mostrar alerta!!!", command=sacarAlerta).pack()

ventana.mainloop()
