from Objetos import objDoctor # Dentro de los módulos hay que importar el archivo, ¡NO LA CLASE!

class Paciente:

    __doctor = None

    # Los parámetros no recibidos son obligatorios y en caso de asignarlos son optativos
    def __init__(self, nombre, edad, enfermedad="-"):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad

    # def __init__(self, obj):
    #     self(obj.getNombre(), obj.getEdad(), obj.getEnfermedad())

    # SETTERS

    def setNombre(self, nombre):
        self.enfermedad = nombre

    def setEdad(self, edad):
        self.enfermedad = edad

    def setEnfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def setDoctor(self, obj):
        doc = objDoctor.Doctor(obj)
        self.__doctor = doc

    # GETTERS

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getEnfermedad(self):
        return self.enfermedad

    def getDoctor(self):
        return self.__doctor

    def getData(self):
        return "Nombre: {}, Edad: {}, Enfermedad: {}".format(
            self.nombre, self.edad, self.enfermedad)

    # Métodos

    def show(self):
        print(self.getData())

    def removeDoctor(self, obj):
        if obj.equals(self.__doctor):
            self.__doctor = None

    def equals(self, obj):
        esIgual = False
        if self.nombre == obj.getNombre() and self.edad == obj.getEdad() and self.enfermedad == obj.getEnfermedad():
            esIgual = True
        return esIgual

    
