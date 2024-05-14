diccionarioUsuarios = {}
diccionarioDeAcciones = {}
dniLogged = "1"

#FUNCIONES
def darAltaUsuario(dni, nombre, apellido):
    global dniLogged  # Utilizamos la declaración global para modificar la variable fuera de la función
    diccionarioUsuarios[dni] = [nombre, apellido]
    diccionarioDeAcciones[dniLogged] = diccionarioDeAcciones.get(dniLogged, []) + ["ALTA"]
    dniLogged = dni  # Cambiamos el DNI logueado al nuevo usuario

def usuarioAdmin():
    diccionarioUsuarios["1"] = ["Admin", "Admin"]

def darBajaUsuario(dniLogged, dni):
    del(diccionarioUsuarios[dni])
    diccionarioDeAcciones[dniLogged] += ["BAJA"]

def modificarUsuario(dniLogged, dni, nombre, apellido):
    diccionarioUsuarios[dni] = [nombre, apellido]
    diccionarioDeAcciones[dniLogged] += ["MODIFICAR"]

def consultarDatosUsuario(dniLogged, dni):
    print("Nombre:", diccionarioUsuarios[dni][0])
    print("Apellido:", diccionarioUsuarios[dni][1])
    diccionarioDeAcciones[dniLogged] += ["CONSULTA"]

usuarioAdmin()
while True:
    print("==== Bienvenido a Sistema CRUD en Python! =====")
    print("")
    print("1. Dar usuario de alta")
    print("2. Dar usuario de baja")
    print("3. Modificar un usuario")
    print("4. Consultar datos de un usuario")
    print("5. Cambiar de usuario")
    print("6. Salir")
    opc = input("-- SELECCIONE UNA OPCION: ")
    # Verificar si la opción ingresada es un número entre 1 y 6
    if opc.isdigit():  # Verifica si la entrada es un dígito
        opc = int(opc)
        if opc == 6:
            print("Saliendo del sistema...")
            break  # Salir del ciclo while
        elif opc >= 1 and opc <= 5:
            # Manejar opciones del 1 al 5 usando un switch
            if opc == 1:
                print("Seleccionaste Dar usuario de alta")
                print("Estas logeado como", diccionarioUsuarios[dniLogged])
                dniAlta = input("| Ingrese DNI: ")
                nombreAlta = input("| Ingrese nombre: ")
                apellidoAlta = input("| Ingrese apellido: ")

                if dniAlta in diccionarioUsuarios:
                    print("DNI EXISTENTE EN EL DICCIONARIO")
                else:
                    darAltaUsuario(dniAlta, nombreAlta, apellidoAlta)
                
            elif opc == 2:
                print("Seleccionaste Dar usuario de baja")
                dniBaja = input("| Ingrese DNI a dar de baja: ")
                if dniBaja != dniLogged:
                    darBajaUsuario(dniLogged, dniBaja)
                else:
                    print("No se puede eliminar a si mismo.")
            elif opc == 3:
                print("Seleccionaste Modificar un usuario")
                # Aquí puedes poner la lógica para modificar un usuario
            elif opc == 4:
                print("Seleccionaste Consultar datos de un usuario")
                dniConsulta = input("| Ingrese DNI a consultar: ")
                if dniConsulta in diccionarioUsuarios:
                    consultarDatosUsuario(dniLogged, dniConsulta)
                else: 
                    ("El DNI ingresado no existe en el sistema.")
            elif opc == 5:
                print("Seleccionaste Cambiar de usuario")
                # Aquí puedes poner la lógica para cambiar de usuario
        else:
            print("Por favor, ingrese una opción válida (1-6).")
    else:
        print("Por favor, ingrese una opción válida (1-6).")
    
