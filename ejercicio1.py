class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado:
    def __init__(self, salario, sucursal):
        self.salario = salario
        self.sucursal = sucursal

class Planta(Persona, Empleado):
    def __init__(self, nombre, edad, nacionalidad, salario, sucursal, bono, saldo_h_extras, desc_seguridad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Empleado.__init__(self, salario, sucursal)
        self.bono = bono
        self.saldo_h_extras = saldo_h_extras
        self.desc_seguridad = desc_seguridad

    def calcular_sueldo(self):
        return self.salario + self.bono + self.saldo_h_extras - self.desc_seguridad

class Contratista(Persona, Empleado):
    def __init__(self, nombre, edad, nacionalidad, salario, sucursal, retefuente):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Empleado.__init__(self, salario, sucursal)
        self.retefuente = retefuente

    def calcular_sueldo(self):
        return self.salario * (1 - self.retefuente / 100)


empleado_planta = Planta("Jesus", 26, "Colombiana", 5000, "Sucursal A", 500, 200, 100)
print(f"Sueldo empleado de planta: {empleado_planta.calcular_sueldo()}")

empleado_contratista = Contratista("Ana", 28, "Mexicana", 4000, "Sucursal B", 3)
print(f"Sueldo empleado contratista: {empleado_contratista.calcular_sueldo()}")
