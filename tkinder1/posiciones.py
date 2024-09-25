from tkinter import*

ventana = Tk()
# ventana.geometry("500x500")
# ventana.resizable(0,0)

texto = Label(ventana, text="bienvenido a mi programa")

texto.config(
        fg="white",
        bg="#000000",
        padx=50,
        pady=20,
        font=("Arial",30)
)
texto.pack(side=TOP) 


texto= Label(ventana, text="soy victor robles")
texto.config(
    
    height=2,
    bg="orange",
    font=("Arial",18),
    padx=18,
    pady=20,
    cursor=("circle",)
   
)
texto.pack(side=TOP,fill=X, expand=YES) 

texto = Label(ventana, text="Basico 1")
texto.config(
    height=2,
    bg="yellow",
    font=("Arial",14),
    padx=10,
    pady=10
)
texto.pack(side=LEFT, fill=X,expand=YES) 


texto = Label(ventana, text="Basico 2")
texto.config(
    height=2,
    bg="green",
    font=("Arial",14),
    padx=10,
    pady=10
)
texto.pack(side=LEFT, fill=X,expand=YES) 


texto = Label(ventana, text="Basico 3")
texto.config(
    height=2,
    bg="orange",
    font=("Arial",14),
    padx=10,
    pady=10
)
texto.pack(side=LEFT, fill=X,expand=YES) 
ventana.mainloop()