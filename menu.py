def mostrarMenu(opciones):
    print ('Seleccione una opcion')
    for i in sorted(opciones):
        print(f' {i}) {opciones[i][0]}')
        
        
def leerOpcion(opciones):
    while (a:= input('Opcion: ')) not in opciones:
        print('Opcion incorrecta, vuelva a intentarlo')
    return a

def ejecutarOpcion(opcion, opciones):
    opciones[opcion][1]()

def generarMenu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrarMenu(opciones)
        opcion = leerOpcion(opciones)
        ejecutarOpcion(opcion, opciones)
        print()#se imprime una linea en blanco para clarificar la salida por pantalla

def pedirOpcion():
    opciones = {
        '1': ('Alta de usuario'),
        '2': ('Baja de usuario'),
        '3': ('Modificar usuario'),
        '4': ('Consultar datos usuario'),
        '5': ('Cambiar de usuario'),
        '6': ('Salir')
    }

    generarMenu(opciones, 4)



