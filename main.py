# Dentro del programa principal se puede importar la clase o módulo.
from funciones.defs import *

if __name__ == '__main__':

    hospitales = []
    doctores = []
    pacientes = []

    seguir = True

    while seguir:
        menu()
        opc = input("Opción: ")
        
        seguir = ejecutarOpcion(opc, hospitales, doctores, pacientes)
