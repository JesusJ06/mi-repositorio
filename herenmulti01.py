class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}."


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}."
    
class Escritor(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, libro):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.libro = libro
    def escribir_novelas(self):
        return f"Escribo en mi libro {self.libro}."
    
# Crear objeto
escritor1= Escritor("Juan",45,"Español","escritura en prosa","El amor en la ocuridad")
print(escritor1.presentarse())
print(escritor1.mostrar_habilidad())
print(escritor1.escribir_novelas())
