from Objetos import objDoctor # Dentro de los módulos hay que importar el archivo, ¡NO LA CLASE!

class Hospital:

    __doctores = []  # Si se ponen 2 "_" delante indica que no es accesible desde el exterior

    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    # def __init__(self, obj):
    #     self(obj.getNombre(), obj.getCiudad())
    #     self.__doctores = obj.getDoctores()

    # SETTERS

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    # GETTERS

    def getNombre(self):
        return self.nombre

    def getCiudad(self):
        return self.ciudad

    def getDoctores(self):
        doctores = []

        for x in self.__doctores:
            doctores.append(x)

        return doctores
    
    def getData(self):
        return "Nombre: {}, Ciudad: {}".format(
            self.getNombre(), self.getCiudad())

    # Métodos

    def show(self):
        print(self.getData())

    

    def addDoctor(self, d1):  # Podemos pasar clases a los métodos
        newDoctor = objDoctor.Doctor(d1.getNombre(), d1.getEdad(), d1.getExpecialidad())
        self.__doctores.append(newDoctor)

    def removeDoctor(self, obj):
        i = 0
        for x in self.__doctores:
            if x.equals(obj):
                self.__doctores.pop(i)
                break
            i += 1

    def showDoctores(self):
        lista = "Doctores: "

        for obj in self.__doctores:
            lista += "{}-{} ".format(obj.getNombre(), obj.getEdad())

        lista = lista[:-1]  # Borra el último caracter de la cadena

        print(lista)

    def equals(self, obj):
        esIgual = False
        if self.getNombre() == obj.getNombre() and self.getCiudad() == obj.getCiudad():
            esIgual = True
        return esIgual
