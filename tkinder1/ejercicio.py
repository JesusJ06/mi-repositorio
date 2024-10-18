from tkinter import *
from tkinter import messagebox

class Calculadora:
    def __init__(self, ventana):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.ventana = ventana  # Guardar la referencia de la ventana

    def cFloat(self, numero):
        try:
            return float(numero)
        except ValueError:
            messagebox.showerror("Error", "Ingresar bien los datos")
            return 0

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        divisor = self.cFloat(self.numero2.get())
        if divisor == 0:
            messagebox.showerror("Error", "No se puede dividir por cero")
        else:
            self.resultado.set(self.cFloat(self.numero1.get()) / divisor)
            self.mostrarResultado()

    def mostrarResultado(self):
        messagebox.showinfo("Resultado", f"El resultado de la operación es: {self.resultado.get()}")

def crear_ventana():
    ventana = Tk()
    ventana.title("Ejercicio completo con Tkinter")
    ventana.geometry("400x400")
    ventana.config(bd=35)

    calculadora = Calculadora(ventana)

    marco = Frame(ventana, width=250, height=250)
    marco.config(padx=15, pady=15, bd=5, relief=SOLID)
    marco.pack(side=TOP, anchor=CENTER)
    marco.pack_propagate(False)

    Label(marco, text="Primer número: ").pack()
    Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

    Label(marco, text="Segundo número: ").pack()
    Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

    Label(marco, text="").pack()

    Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
    Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
    Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
    Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

    ventana.mainloop()

crear_ventana()
