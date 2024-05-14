# Función para mostrar el menú de opciones
def mostrar_menu():
    print("==== Menú de opciones ====")
    print("a. Dar un usuario de alta")
    print("b. Dar un usuario de baja")
    print("c. Modificar un usuario")
    print("d. Consultar los datos de un usuario")
    print("e. Cambiar de usuario")
    print("f. Salir")

# Función para solicitar una opción válida al usuario
def pedir_opcion():
    opciones_validas = ['a', 'b', 'c', 'd', 'e', 'f']
    while True:
        opcion = input("Ingrese una opción (a-f): ").lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print("Ingrese una opción válida.")

# Función para verificar si el usuario desea salir
def quiere_salir():
    respuesta = input("¿Está seguro que desea salir? (S/N): ").upper()
    return respuesta == 'S'

# Función para dar de alta a un usuario
def dar_alta_usuario(diccionario_usuarios, dni_logged):
    dni = input("Ingrese el DNI del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    if dni in diccionario_usuarios:
        diccionario_usuarios[dni]["acciones"].append("ALTA")
    else:
        diccionario_usuarios[dni] = {"nombre": nombre, "apellido": apellido, "acciones": ["ALTA"]}
    print("Usuario dado de alta con éxito.")

# Función para dar de baja a un usuario
def dar_baja_usuario(diccionario_usuarios, dni_logged):
    dni_baja = input("Ingrese el DNI del usuario a dar de baja: ")
    if dni_baja != dni_logged:
        if dni_baja in diccionario_usuarios:
            diccionario_usuarios[dni_baja]["acciones"].append("BAJA")
            del diccionario_usuarios[dni_baja]
            print("Usuario dado de baja con éxito.")
        else:
            print("El usuario no existe en el sistema.")
    else:
        print("No puede eliminar su propio usuario.")

# Función para modificar un usuario
def modificar_usuario(diccionario_usuarios, dni_logged):
    dni_modificar = input("Ingrese el DNI del usuario a modificar: ")
    if dni_modificar in diccionario_usuarios:
        nombre = input("Ingrese el nuevo nombre del usuario: ")
        apellido = input("Ingrese el nuevo apellido del usuario: ")
        diccionario_usuarios[dni_modificar]["nombre"] = nombre
        diccionario_usuarios[dni_modificar]["apellido"] = apellido
        diccionario_usuarios[dni_modificar]["acciones"].append("MODIFICAR")
        print("Usuario modificado con éxito.")
    else:
        print("El usuario no existe en el sistema.")

# Función para consultar los datos de un usuario
def consultar_datos_usuario(diccionario_usuarios, dni_logged):
    dni_consulta = input("Ingrese el DNI del usuario a consultar: ")
    if dni_consulta in diccionario_usuarios:
        usuario = diccionario_usuarios[dni_consulta]
        print("Nombre:", usuario["nombre"])
        print("Apellido:", usuario["apellido"])
        print("Acciones realizadas:", usuario["acciones"])
    else:
        print("El usuario no existe en el sistema.")

# Función para cambiar de usuario
def cambiar_usuario(diccionario_usuarios, dni_logged):
    nuevo_dni = input("Ingrese el DNI del nuevo usuario: ")
    if nuevo_dni in diccionario_usuarios:
        print("Cambiando de usuario...")
        return nuevo_dni
    else:
        print("El usuario no existe en el sistema.")
        return dni_logged

# Función principal del programa
def main():
    diccionario_usuarios = {}
    dni_logged = None
    
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 'a':
            dar_alta_usuario(diccionario_usuarios, dni_logged)
        elif opcion == 'b':
            dar_baja_usuario(diccionario_usuarios, dni_logged)
        elif opcion == 'c':
            modificar_usuario(diccionario_usuarios, dni_logged)
        elif opcion == 'd':
            consultar_datos_usuario(diccionario_usuarios, dni_logged)
        elif opcion == 'e':
            dni_logged = cambiar_usuario(diccionario_usuarios, dni_logged)
        elif opcion == 'f':
            if quiere_salir():
                print("Saliendo del programa...")
                break
            else:
                continue

# Ejecutar el programa
if __name__ == "__main__":
    main()