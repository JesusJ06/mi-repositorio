class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.nacionalidad = nacionalidad

    
class Cliente(Persona):
    def __init__(self, nombre, edad, nacionalidad, compra, descuento):
        super().__init__(nombre, edad, nacionalidad)
        self.__compra = compra
        self.__descuento = descuento
        self.cambiar_des()
    
    @property
    def compra(self):
        return self.__compra
    
    @property
    def descuento(self):
        return self.__descuento
    
    @descuento.setter
    def descuento(self,nuevo_descuento):
         self.__descuento = nuevo_descuento

    def cambiar_des(self):
        if self.__compra>300:
          self.__descuento=0.2
        else:
            self.__descuento=0.1

cliente1=Cliente("Libia",34,"Argentina",200,0.1)

print (f"el descuento es: {cliente1.descuento}")

