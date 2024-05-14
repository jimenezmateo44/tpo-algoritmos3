diccionarioUsuarios = {}
diccionarioDeAcciones = {}

#a
def darAltaUsuario(dniLogged, dni, nombre, apellido):
    diccionarioUsuarios[dni] = [nombre, apellido]
    if dniLogged in diccionarioDeAcciones:
        diccionarioDeAcciones[dniLogged] += ["ALTA"]
    else:
        diccionarioDeAcciones[dniLogged] = ["ALTA"]


#b
def darBajaUsuario(dniLogged, dni):
    del(diccionarioUsuarios[dni])
    diccionarioDeAcciones[dniLogged] += ["BAJA"]


#c
def modificarUsuario(dniLogged, dni, nombre, apellido):
    diccionarioUsuarios[dni] = [nombre, apellido]
    diccionarioDeAcciones[dniLogged] += ["MODIFICAR"]

#d
def consultarDatosUsuario(dniLogged, dni):
    print("Nombre:", diccionarioUsuarios[dni][0])
    print("Apellido:", diccionarioUsuarios[dni][1])
    diccionarioDeAcciones[dniLogged] += ["CONSULTA"]


darAltaUsuario("1","42065172","Mateo","Jimenez")

print(diccionarioUsuarios)
print(diccionarioDeAcciones)

    


