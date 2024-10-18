import tkinter  as tk
from tkinter import messagebox
import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname="JJ",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        print("Conectar exitosamente")
        return conn
    except psycopg2.Error as e:
        messagebox.showerror("Error de conexion", f"No se puedo conectar a la base de datos")
        exit()

def agregar_venta():
    id= entry_id.get()
    nombre= entry_nombre.get()
    venta= entry_venta.get()
    sucursal= entry_sucursal.get()

    if id and nombre and venta and sucursal:
        try:
            conn = conectar_db()
            c= conn.cursor()
            c.execute("INSERT INTO venta (id, nombre, venta, sucursal) VALUES (%s, %s, %s, %s)",
                        (id, nombre, venta, sucursal))
            conn.commit()
            c.close()
            conn.close()
            messagebox.showinfo("Exito", "Registro agregado exitosamente")
            limpiar_formulario()
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo agregar la ventana: {e}")
    else:
        messagebox.showwarning("Error", "Por favor complete todos los campos")

#limpiar el formulario despues de agregar los datos
def limpiar_formulario(): 
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_venta.delete(0, tk.END)
    entry_sucursal.delete(0, tk.END)


#ventana para consultar por ID
def abrir_ventana_consulta():
    consulta_ventana = tk.Toplevel(root)
    consulta_ventana.title("Consulta de ventas por ID")
    consulta_ventana.geometry("300x200")

    tk.Label(consulta_ventana, text="Ingresar el ID").pack(pady=10)
    entry_id_consulta = tk.Entry(consulta_ventana)
    entry_id_consulta.pack()

    def consultar():
        id_consulta = entry_id_consulta.get()
        if id_consulta:
            try:
                conn = conectar_db()
                c= conn.cursor()
                c.execute("SELECT * FROM venta WHERE id=%s", (id_consulta,))
                resultado = c.fetchone()
                conn.close()

                if resultado:
                    mensaje = f"ID:{resultado[0]}\nnombre: {resultado[1]}\nventa: {resultado[2]}\nsurcurlsal: [resultado{3}]"
                    messagebox.showinfo("resultado de la consulta",mensaje)
                else:
                    messagebox.showinfo("Advertencia","no  se encontro una venta con ese ID")

            except psycopg2.Error as e:
                messagebox.showerror("Error", f"Error en la consulta:{e}")

        else:
            messagebox.showwarning("Advertencia","por favor, ingrese un ID" )

    btn_consultar=tk.Button(consulta_ventana, text ="consultar", command = consultar)
    btn_consultar.pack(pady=20)

def actualizar_venta():
    id_actualizar = entry_id.get()
    nombre_actualizar = entry_nombre.get()
    venta_actualizar = entry_venta.get()
    sucursal_actualizar = entry_sucursal.get()
    if nombre_actualizar and venta_actualizar and sucursal_actualizar:
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE venta SET nombre=%s, venta=%s, sucursal=%s WHERE id=%s", (nombre_actualizar, venta_actualizar, sucursal_actualizar, id_actualizar))
            conn.commit()
            messagebox.showinfo("exito", "ventana actualizada correctamente")
            limpiar_formulario()
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar la ventana: {e}")

def eliminar_venta():
    id_eliminar = entry_id.get()
    if id_eliminar:
        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM venta WHERE id=%s", (id_eliminar,))
            conn.commit()
            messagebox.showinfo("exito", "ventana eliminada correctamente")
            limpiar_formulario()
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"No se pudo eliminar la ventana: {e}")
    else:
        messagebox.showerror("Error", "El ID es obligatorio")

#configuracion de la ventana principal
root = tk.Tk()
root.title("Registro de ventas")
root.geometry("300x250")

#crear_tabla

# Etiquetas y campos de entrada
tk.Label(root, text="ID").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Nombre").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Ventas").pack(pady=5)
entry_venta = tk.Entry(root)
entry_venta.pack()

tk.Label(root, text="Sucursal").pack(pady=5)
entry_sucursal = tk.Entry(root)
entry_sucursal.pack()

# Botones para agregar la ventana
btn_agregar = tk.Button(root, text="Agregar ventana", command= agregar_venta)
btn_agregar.pack(pady=10)


# Boton para abrir la ventana de consulta
btn_consultar = tk.Button(root, text="Consultar por ID", command=abrir_ventana_consulta)
btn_consultar.pack(pady=10)

eliminar_boton = tk.Button(root, text="Eliminar Venta", command=eliminar_venta)
eliminar_boton.pack(pady=10)

limpiar_boton = tk.Button(root, text="limpiar Formulario", command=limpiar_formulario)
limpiar_boton.pack(pady=10)


actualizar_boton = tk.Button(root, text="Actualizar Venta", command=actualizar_venta)
actualizar_boton.pack(pady=10)

#ejecutar la aplicacion
root.mainloop()