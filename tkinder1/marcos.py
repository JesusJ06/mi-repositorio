from tkinter import *

ventana= Tk()
ventana.title("Marco | Master en python")
ventana.geometry("700x400")

marco= Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
     bd=12,
     relief="groove"
)

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

Label(marco, text="primer marco").pack(anchor=SE)





ventana.mainloop()



