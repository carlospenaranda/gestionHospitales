from Objetos.objHospital import Hospital
from Objetos.objDoctor import Doctor
from Objetos.objPaciente import Paciente


def menu():
    print("==== ELIGE UNA OPCIÓN ====")
    print("  1. Crear objetos        ")
    print("  2. Eliminar objetos     ")
    print("  3. Editar objetos       ")
    print("  4. Salir                ")
    print("==========================")


def menu2():
    print("==== ELIGE UNA OPCIÓN ====")
    print("  1. Hospital             ")
    print("  2. Doctor               ")
    print("  3. Paciente             ")
    print("  4. Salir                ")
    print("==========================")


def mostrarArray(array):
    i = 1
    for h in array:
        print("{}. {}".format(i, h.getData()))
        i += 1


def ejecutarOpcion(opc, hospitales, doctores, pacientes):
    seguir = True

    if opc == "1":  # CREAR
        menu2()
        opc2 = input("Opción: ")
        if opc2 == "1":
            # HOSPITAL

            nombreHospital = input("- Nombre del hospital: ")
            ciudadHospital = input("- Ciudad: ")

            hospital = Hospital(nombreHospital, ciudadHospital)

            if len(doctores) > 0:
                print("Lista de doctores sin hospital asignado:")
                docSinHospital = []

                for d in doctores:
                    if d.getHospital() == None:
                        docSinHospital.append(d)

                mostrarArray(docSinHospital)

                docElegido = int(
                    input("- Doctor elegido: ") - 1)
                
                doctor = docSinHospital[docElegido]

                hospital.addDoctor(doctor)
                doctor.setHospital(hospital)

                print("- ¡Doctor asignado!")
            else:
                print("- No hay doctores sin hospital")

            hospitales.append(hospital)

            hospital.show()
            print("¡Hospital añadido a lista!\n")
        else:
            if opc2 == "2":
                # DOCTOR

                nombreDoctor = input("- Nombre del doctor: ")
                edadDoctor = int(input("- Edad: "))
                expecialidad = input("- Expecialidad: ")

                doctor = Doctor(nombreDoctor, edadDoctor, expecialidad)

                if len(hospitales) > 0:
                    print("Lista de hospitales:")
                    mostrarArray(hospitales)
                    hosElegido = int(input("- Hospital elegido: ")) - 1
                    hospital = hospitales[hosElegido]
                    doctor.setHospital(hospital)
                    hospital.addDoctor(doctor)
                else:
                    print("- No hay hospitales para asignar")

                doctores.append(doctor)
                doctor.show()
                print("Doctor añadido a lista!\n")
            else:
                if opc2 == "3":
                    # PACIENTE
                    nombrePaciente = input("- Nombre del paciente: ")
                    edadPaciente = int(input("- Edad: "))
                    enfermedad = input("- Enfermedad: ")

                    paciente = Paciente(
                        nombrePaciente, edadPaciente, enfermedad)

                    if len(doctores) > 0:
                        print("Lista de doctores:")
                        mostrarArray(doctores)

                        docElegido = int(
                            input("- Doctor elegido: ") - 1)
                        
                        doctor = doctores[docElegido]

                        paciente.setDoctor(doctor)
                        print("- ¡Doctor asignado!")
                    else:
                        print("- No hay doctores")

                    pacientes.append(paciente)
                    paciente.show()

                    print("Paciente añadido a lista!\n")
    else:
        if opc == "2":  # ELIMINAR
            menu2()
            opc2 = input("Opción: ")
            if opc2 == "1":
                # HOSPITALES

                if len(hospitales) > 0:
                    print("Lista de hospitales:")
                    mostrarArray(hospitales)
                    hosElegido = int(input("Nº hospital: ")) - 1
                    hospital = hospitales[hosElegido]

                    for doctor in doctores:
                        hosDoctor = doctor.getHospital()
                        if hosDoctor.equals(hospital):
                            doctor.setHospital(None)

                    hospitales.remove(hospital)
                    print("- ¡Hospital eliminado!")
                else:
                    print("No hay hospitales")
            else:
                if opc2 == "2":
                    # DOCTORES
                    if len(doctores) > 0:
                        print("Lista de doctores:")
                        mostrarArray(doctores)
                        docElegido = int(input("Nº doctor: ")) - 1
                        doctor = doctores[docElegido]

                        for hospital in hospitales:
                            hospital.removeDoctor(doctor)

                        for paciente in pacientes:
                            paciente.removeDoctor(doctor)

                        doctores.remove(doctor)
                        print("- ¡Doctor eliminado!")
                    else:
                        print("No hay doctores")

                else:
                    if opc2 == "3":
                        # PACIENTES
                        if len(pacientes) > 0:
                            print("Lista de pacientes:")
                            mostrarArray(pacientes)
                            pacElegido = int(input("Nº paciente: ")) - 1
                            paciente = pacientes[pacElegido]

                            pacientes.remove(paciente)
                            print("- ¡Paciente eliminado!")
                        else:
                            print("No hay pacientes")
        else:
            if opc == "3":  # EDITAR
                menu2()
                opc2 = input("Opción: ")
                if opc2 == "1":  # HOSPITAL

                    if len(hospitales) > 0:
                        print("Lista de hospitales:")
                        mostrarArray(hospitales)
                        hosElegido = int(input("- Hospital a editar: ")) - 1

                        hospital = hospitales[hosElegido]

                        print("==== ELIGE UNA OPCIÓN ====")
                        print("  1. Nombre               ")
                        print("  2. Ciudad               ")
                        print("  3. Doctores             ")
                        print("  4. Salir                ")
                        print("==========================")

                        opc3 = input("- Elige una opción: ")

                        if opc3 == "1":
                            newNombre = input("- Nuevo nombre: ")
                            hospital.setNombre(newNombre)
                            print("- ¡Nombre cambiado!")
                            hospital.show()
                        else:
                            if opc3 == "2":
                                newCiudad = input("- Nueva ciudad: ")
                                hospital.setCiudad(newCiudad)
                                print("- ¡Ciudad cambiada!")
                                hospital.show()
                            else:
                                if opc3 == "3":

                                    print("==== ELIGE UNA OPCIÓN ====")
                                    print("  1. Añadir               ")
                                    print("  2. Eliminar             ")
                                    print("  4. Salir                ")
                                    print("==========================")

                                    opc4 = input("- Opción: ")

                                    if opc4 == "1":  # AÑADIR DOCTOR

                                        if len(doctores) > 0:

                                            print(
                                                "- Lista de doctores que no tienen hospital: ")

                                            docSinHospital = []

                                            for d in doctores:
                                                if d.getHospital() == None:
                                                    docSinHospital.append(d)

                                            mostrarArray(docSinHospital)

                                            docElegido = int(
                                                input("- Doctor elegido: ") - 1)

                                            docSinHospital[docElegido].setHospital(
                                                hospital)

                                            print(
                                                "- ¡Doctor añadido al hospital!")
                                            mostrarArray(
                                                hospital.getDoctores())
                                        else:
                                            print(
                                                "- No hay doctores para añadir")

                                    else:
                                        if opc4 == "2":  # ELIMINAR DOCTOR
                                            listaDoctoresHospital = hospital.getDoctores()
                                            mostrarArray(listaDoctoresHospital)
                                            docElegido = int(
                                                input("- Elige un doctor: " - 1))
                                            hospital.removeDoctor(
                                                listaDoctoresHospital[docElegido])
                                            print(
                                                " - ¡Doctor elimimnado del hospital!")
                                            mostrarArray(
                                                hospital.getDoctores())
                                        else:
                                            seguir = False

                    else:
                        print("- No hay hospitales para editar")
                else:
                    if opc2 == "2":  # DOCTOR
                        if len(doctores) > 0:

                            print("Lista de doctores:")
                            mostrarArray(doctores)
                            docElegido = int(input("- Doctor a editar:")) - 1

                            doctor = doctores[docElegido]

                            print("==== ELIGE UNA OPCIÓN ====")
                            print("  1. Nombre               ")
                            print("  2. Edad                 ")
                            print("  3. Expecialidad         ")
                            print("  4. Hospital             ")
                            print("  5. Salir                ")
                            print("==========================")

                            opc3 = input("- Elige una opción: ")

                            if opc3 == "1":
                                newNombre = input("- Nuevo nombre: ")
                                doctor.setNombre(newNombre)
                                print("- ¡Nombre cambiado!")
                                doctor.show()
                            else:
                                if opc3 == "2":
                                    newEdad = int(input("- Nueva edad: "))
                                    doctor.setEdad(newEdad)
                                    print("- ¡Edad cambiada!")
                                    doctor.show()
                                else:
                                    if opc3 == "3":
                                        newExpecialidad = input(
                                            "- Nueva expecialidad: ")
                                        doctor.setExpecialidad(newExpecialidad)
                                        print("- ¡Expecialidad cambiada!")
                                        doctor.show()
                                    else:
                                        if opc3 == "4":
                                            if len(hospitales) > 0:
                                                print("Lista de hospitales:")
                                                mostrarArray(hospitales)
                                                hosElegido = int(
                                                    input("- Hospital a asignar: ")) - 1
                                                hospital = hospitales[hosElegido]
                                                doctor.setHospital(hospital)
                                            else:
                                                print(
                                                    "- No hay hospitales para ser asignados")

                        else:
                            print("- No hay doctores para editar")
                    else:
                        if opc2 == "3":  # PACIENTE
                            if len(pacientes) > 0:
                                print("Lista de pacientes:")
                                mostrarArray(pacientes)
                                pacElegido = int(
                                    input("- Paciente a editar: ")) - 1
                                paciente = pacientes[pacElegido]

                                print("==== ELIGE UNA OPCIÓN ====")
                                print("  1. Nombre               ")
                                print("  2. Edad                 ")
                                print("  3. Enfermedad           ")
                                print("  4. Doctor               ")
                                print("  5. Salir                ")
                                print("==========================")

                                opc3 = input("- Opción: ")

                                if opc3 == "1":
                                    newNombre = input("- Nuevo nombre: ")
                                    paciente.setNombre(newNombre)
                                    print("- ¡Nombre cambiado!")
                                    paciente.show()
                                else:
                                    if opc3 == "2":
                                        newEdad = int(input("- Nueva edad: "))
                                        paciente.setEdad(newEdad)
                                        print("- ¡Edad cambiada!")
                                        paciente.show()
                                    else:
                                        if opc3 == "3":
                                            newEnfermedad = input(
                                                "- Nueva enfermedad: ")
                                            paciente.setEnfermedad(
                                                newEnfermedad)
                                            print("- ¡Enfermedad cambiada!")
                                            paciente.show()
                                        else:
                                            if opc3 == "4":
                                                print(
                                                    "==== ELIGE UNA OPCIÓN ====")
                                                print(
                                                    "  1. Añadir               ")
                                                print(
                                                    "  2. Eliminar             ")
                                                print(
                                                    "  4. Salir                ")
                                                print(
                                                    "==========================")

                                                opc4 = input("- Opción: ")

                                                if opc4 == "1":
                                                    if len(doctores) > 0:
                                                        print(
                                                            "Lista de doctores:")
                                                        mostrarArray(doctores)
                                                        docElegido = int(
                                                            input("- Elige un doctor: ")) - 1
                                                        doctor = doctores[docElegido]
                                                        paciente.setDoctor(
                                                            doctor)
                                                        print(
                                                            "- ¡Doctor actualizado!")
                                                        paciente.show()

                                                    else:
                                                        print(
                                                            "- No hay doctores")
                                                else:
                                                    if opc4 == "2":
                                                        doctorActual = paciente.getDoctor()
                                                        if doctorActual == None:
                                                            print(
                                                                "El paciente no tiene doctor asignado")
                                                        else:
                                                            paciente.setDoctor(
                                                                None)
                                                            print(
                                                                "- ¡Doctor eliminado!")
                                                            paciente.show()

                            else:
                                print("- No hay pacientes creados")
                        else:
                            seguir = False
    return seguir
