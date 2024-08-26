class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario, area):
        super().__init__(nombre, edad)
        self.salario = salario
        self.area = area

class Cliente(Persona):
    def __init__(self, nombre, edad, compra, bono):
        super().__init__(nombre, edad)
        self.compra = compra
        self.bono = bono

class Vendedor(Empleado):
    def __init__(self, nombre, edad, salario, area, venta, sucursal):
        super().__init__(nombre, edad, salario, area)
        self.venta = venta
        self.sucursal = sucursal

    def calcular_comision(self):
        return self.venta * 0.11

    def calcular_venta_con_descuento(self):
        return self.venta * 0.90

vendedor1 = Vendedor(nombre="Jesus", edad=25, salario=6000, area="Vendedor", venta=1000, sucursal="Central")

comision = vendedor1.calcular_comision()
venta_con_descuento = vendedor1.calcular_venta_con_descuento()

print(f"Venta con descuento aplicada a la compra del cliente: {venta_con_descuento}")
print(f"El empleado {vendedor1.nombre} ganó una comisión de {comision} por sus ventas.")