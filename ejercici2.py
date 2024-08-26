class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario 

    def obtener_salario(self):
        return self.__salario

    def establecer_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

class Vendedor(Empleado):
    def __init__(self, nombre, edad, salario, ventas):
        super().__init__(nombre, edad, salario)
        self.__ventas = ventas 
    def obtener_ventas(self):
        return self.__ventas

    def verificar_y_modificar_salario(self):
        if self.obtener_ventas() >= 5000:
            nuevo_salario = self.obtener_salario() + 100
            self.establecer_salario(nuevo_salario)

vendedor = Vendedor("Juan", 30, 1500, 6000)
vendedor.verificar_y_modificar_salario()

print(f"Nombre: {vendedor.nombre}")
print(f"Edad: {vendedor.edad}")
print(f"Salario: {vendedor.obtener_salario()} USD")
print(f"Ventas: {vendedor.obtener_ventas()} USD")


# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad

# class Empleado(Persona):
#     def __init__(self, nombre, edad, salario):
#         super().__init__(nombre, edad)
#         self._salario = salario

#     @property
#     def salario(self):
#         return self._salario

#     @salario.setter
#     def salario(self, nuevo_salario):
#         self._salario = nuevo_salario

# class Vendedor(Empleado):
#     def __init__(self, nombre, edad, salario,venta):
#         super().__init__(nombre, edad, salario)
#         self._venta = venta
         

#     @property
#     def ventas(self):
#         return self._venta
    
#     @ventas.setter
#     def ventas(self, nuevas_ventas):
#         self._venta = nuevas_ventas
#         if self._venta >= 5000:
#             self.salario += 100 

   

# vendedor = Vendedor("Juan", 30, 1500,5000)
# print(f"Salario inicial: {vendedor.salario} USD")

# vendedor.ventas = 5000
# print(f"Salario después de ventas: {vendedor.salario} USD")
