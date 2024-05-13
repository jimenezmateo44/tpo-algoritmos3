

diccionarioUsuarios = {}

#a
def darAltaUsuario(diccionarioUsuarios, dni, nombre, apellido):
    diccionarioUsuarios[dni] = [nombre, apellido]

#b
def darBajaUsuario(diccionarioUsuarios, dni):
    del(diccionarioUsuarios[dni])

#c
def modificarUsuario(diccionarioUsuarios, dni, nombre, apellido):
    diccionarioUsuarios[dni] = [nombre, apellido]

#d
def consultarDatosUsuario(diccionarioUsuarios, dni):
    print("Nombre:", diccionarioUsuarios[dni][0])
    print("Apellido:", diccionarioUsuarios[dni][1])



