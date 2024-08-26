# class X:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def saludar(self):
#         print("saludar")

# class Y(X):
#     def __init__(self,a,b,c,s,t):
#         super().__init__(a,b,c)
#         self.s=s
#         self.t=t


# yx=Y(1,2,3,"luz","liz")
# yx.saludar()

class Persona:
    def __init__(self, nombre, edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi edad es {self.edad} y soy de {self.nacionalidad}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, carrera,n1,n2,n3):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def promedio(self):
        return (self.n1 + self.n2 + self.n3) / 3
    
estudiante1=Estudiante("Jesus",17,"Colombia",4,5,5)
estudiante1.saludar()
promedio=estudiante1.promedio()

print(f"el promedio de notas del estudiante es: {promedio}")