class X:
    def __init__(self,a,b):
        self.__a=a
        self.b=b
    
    def get_a(self):
        return self.__a
    
    def set_a(self,aa):
         self.__a = aa


    

x1= X(3,"hola")
print(x1.get_a())
x1.set_a(23)
print(x1.get_a())

