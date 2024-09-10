import psycopg2

conetar= None
try:

    conectar = psycopg2.connect(
        dbname='Jesus',
        user="postgres", 
        password="123456", 
        host="localhost", 
        port="5432"
    )
    print("Conectado a PostgresSQL")
    cur =conectar.cursor()
    cur.execute("SELECT * FROM ventas")
    for id, nombre, estrato, venta, mes, in cur.fetchall():
        print(id, nombre,estrato,mes, venta, mes)

    cur.close()

except Exception as e:
    print("Error de conexion a PostgresSQL", e)
    if conectar is not None:
     conectar.close()