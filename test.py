def programaPrincipal():

    diccionarioUsuarios = {}
    diccionarioDeAcciones = {}
    dniLogged = "1"
    #a
    def darAltaUsuario(dniLogged, dni, nombre, apellido):
        if dni in diccionarioUsuarios:
            print("El DNI ya existe.")
        else:    
            diccionarioUsuarios[dni] = [nombre, apellido]
        if dniLogged in diccionarioDeAcciones:
            diccionarioDeAcciones[dniLogged] += ["ALTA"]
        else:
            diccionarioDeAcciones[dniLogged] = ["ALTA"]


    #b
    def darBajaUsuario(dniLogged, dni):
        if dniLogged == dni:
            print("No se puede eliminar a si mismo.")
        else:
            if dni in diccionarioUsuarios:
                del(diccionarioUsuarios[dni])
                if dniLogged in diccionarioDeAcciones:
                    diccionarioDeAcciones[dniLogged] += ["BAJA"] 
                else:
                    diccionarioDeAcciones[dniLogged] = ["BAJA"]
            else: 
                print("El DNI indicado no existe en el sistema")
            


    #c
    def modificarUsuario(dniLogged, dni, nombre, apellido):
        diccionarioUsuarios[dni] = [nombre, apellido]
        if dniLogged in diccionarioDeAcciones:
            diccionarioDeAcciones[dniLogged] += ["MODIFICAR"]
        else:
            diccionarioDeAcciones[dniLogged] = ["MODIFICAR"]

    #d
    def consultarDatosUsuario(dniLogged, dni):
        print("Nombre:", diccionarioUsuarios[dni][0])
        print("Apellido:", diccionarioUsuarios[dni][1])
        if dniLogged in diccionarioDeAcciones:
            diccionarioDeAcciones[dniLogged] += ["CONSULTA"]
        else:
            diccionarioDeAcciones[dniLogged] = ["CONSULTA"]
        if not dni in diccionarioDeAcciones:
            print("El usuario consultado no realizo acciones")
        else:
            print(diccionarioDeAcciones[dni])

    #e
    def cambiarUsuario(dni):
        global dniLogged 
        dniLogged = dni
        print("Cambio de sesion a", diccionarioUsuarios[dni])
    
    def usuarioAdmin():
        diccionarioUsuarios["1"] = ["Admin", "Admin"]


    usuarioAdmin()
    #Menu de opciones
    while True:
        print("==== Bienvenido a Sistema CRUD en Python! =====")
        print("")
        print("1. Dar usuario de alta")
        print("2. Dar usuario de baja")
        print("3. Modificar un usuario")
        print("4. Consultar datos de un usuario")
        print("5. Cambiar de usuario")
        print("6. Salir")
        print("")
        print("-----------------------------------------------")
        print("")
        opc = input("-- SELECCIONE UNA OPCION: ")

        if opc.isdigit():  
            opc = int(opc)
            if opc == 6:
                print("Saliendo del sistema...")
                break  
            elif opc >= 1 and opc <= 5:
                if opc == 1:
                    print("Seleccionaste Dar usuario de alta")
                    print("Estas logeado como", diccionarioUsuarios[dniLogged])
                    dniAlta = input("| Ingrese DNI: ")
                    nombreAlta = input("| Ingrese nombre: ")
                    apellidoAlta = input("| Ingrese apellido: ")

                    if dniAlta in diccionarioUsuarios:
                        print("-------------------------------")
                        print("DNI EXISTENTE EN EL DICCIONARIO")
                        print("-------------------------------")
                        print("")
                    else:
                        darAltaUsuario(dniLogged, dniAlta, nombreAlta, apellidoAlta)
                    
                elif opc == 2:
                    print("Seleccionaste Dar usuario de baja")
                    dniBaja = input("| Ingrese DNI a dar de baja: ")
                    if dniBaja != dniLogged and dniBaja in diccionarioUsuarios:
                            darBajaUsuario(dniLogged, dniBaja)
                            print("-------------------------------")
                            print("Usuario eliminado correctamente")
                            print("-------------------------------")
                            print("")
                    else:
                        print("No se puede eliminar a si mismo o no existe.")
                elif opc == 3:
                    print("Seleccionaste Modificar un usuario")
                    dniCambio = input("Ingrese DNI de usuario a modificar: ")
                    nombreCambio = input("| Ingrese nuevo nombre: ")
                    apellidoCambio = input("| Ingrese nuevo apellido: ")
                    modificarUsuario(dniLogged, dniCambio, nombreCambio, apellidoCambio)
                    print("-------------------------------")
                    print("Usuario modificado con exitos!")
                    print("-------------------------------")
                    print("")
                elif opc == 4:
                    print("Seleccionaste Consultar datos de un usuario")
                    dniConsulta = input("| Ingrese DNI a consultar: ")
                    if not dniConsulta in diccionarioUsuarios:
                        print("-----------------------------------------")
                        print("El DNI ingresado no existe en el sistema.")
                        print("-----------------------------------------")
                        print("")
                    else: 
                        consultarDatosUsuario(dniLogged, dniConsulta)      
                elif opc == 5:
                    print("Seleccionaste Cambiar de usuario")
                    dniCambio = input("| Ingrese DNI para cambio de sesion: ")
                    if dniCambio in diccionarioUsuarios:
                        dniLogged = dniCambio
                        cambiarUsuario(dniCambio)
                    else:
                        print("------------------------------------")
                        print("El usuario no existe o fue eliminado")
                        print("------------------------------------")
                        print("")
            else:
                print("Por favor, ingrese una opción válida (1-6).")
                print("")
        else:
            print("Por favor, ingrese una opción válida (1-6).")
            print("")
        

programaPrincipal()
            


