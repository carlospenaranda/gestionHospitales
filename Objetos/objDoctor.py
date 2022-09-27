from Objetos import objHospital # Dentro de los módulos hay que importar el archivo, ¡NO LA CLASE!

class Doctor: 

    __hospital = None

    # Los parámetros no recibidos son obligatorios y en caso de asignarlos son optativos
    def __init__(self, nombre, edad, expecialidad="-"):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setExpecialidad(expecialidad)

    # def __init__(self, obj):
    #     self(obj.getNombre(), obj.getEdad(), obj.getExpecialidad)
    #     self.__hospital = obj.getHospital()

    # SETTERS

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setExpecialidad(self, expecialidad):
        self.expecialidad = expecialidad

    def setHospital(self, obj):
        hospital = objHospital.Hospital(obj)
        self.__hospital = hospital

    # GETTERS

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getExpecialidad(self):
        return self.expecialidad

    def getHospital(self):
        return self.__hospital

    def getData(self):
        return "Nombre: {}, Edad: {}, Expecialidad: {}, Hospital: {}".format(
            self.getNombre(), self.getEdad(), self.getExpecialidad(), self.getHospital())

    # Métodos

    def show(self):
        print(self.getData())

    def equals(self, obj):
        esIgual = False
        if self.getNombre() == obj.getNombre() and self.getEdad() == obj.getEdad() and self.getExpecialidad() == obj.getExpecialidad():
            esIgual = True
        return esIgual
