# Equipo 6 - SISTEMA DE GESTION DE MEMBRESIAS PARA UN GYM.

#CONSTANTES PARA LAS OPCIONES DEL MENÚ
OPCION_NUEVA_CUENTA = 1
OPCION_INICIAR_SESION = 2
OPCION_VER_PLANES = 3
OPCION_ELIMINAR_CUENTA = 4
OPCION_SALIR = 5

#CONSTANTES PARA LOS PRECIOS DE LOS PLANES
PLAN_BASICO = 800
PLAN_ECONOMICO = 1000
PLAN_PREMIUM = 2500
PLAN_BLACK_VIP = 4500

lista_usuarios = []
sesion_activa = None

#FUNCIONES
#Busca al usuario en la lista global. retorna el usuario si todo coincide, si no, retorna None.
def buscar_usuario(usuario_ingresado, contrasenia_ingresada):
    for i in lista_usuarios: 
        if i["usuario"] == usuario_ingresado and i["contrasenia"] == contrasenia_ingresada:
            return i
    return None
    

def iniciar_sesion():
    global sesion_activa
    print("\n --- INICIO DE SESIÓN ---")
    usuario = input("Ingrese su usuario: ")
    contrasenia = input("Ingrese su contraseña: ")

    usuario_encontrado = buscar_usuario(usuario, contrasenia)

    if usuario_encontrado is not None:
        sesion_activa = usuario_encontrado
        print(f"\n¡Inicio de sesión exitoso! Bienvenido {sesion_activa['nombre']}.")

        if sesion_activa["plan"] in ["Premium", "VIP"]:
            print("¡Bienvenido miembro especial! 👑")

            print(f"Resumen de cuenta -> Plan actual: {sesion_activa['plan']}")
        else:
            print("\nError usuario o contraseña incorrectos.")

        reintentar = input("¿Desea reintentar? (si/no): ").strip().upper()
        if reintentar == "si": 
            iniciar_sesion() #Vuelve a llamarse a sí misma para reintentar



#PROCEDIMEINTOS 
def mostrar_menu():
    print("======================================")
    print("=======       BIENVENIDO     =========")
    print("======================================")
    print("** Sistema de gestion de membresias **")
    print("\n--- Menú principal ---")
    print(f"{OPCION_NUEVA_CUENTA}. Registrar nueva cuenta")
    print(f"{OPCION_INICIAR_SESION}. Iniciar sesión")
    print(f"{OPCION_VER_PLANES}. Ver planes de membresía")
    print(f"{OPCION_ELIMINAR_CUENTA}. Eliminar cuenta")
    print(f"{OPCION_SALIR}. salir")
    print("===================================")
    print("\n ELIJA UNA OPCION PARA CONTINUAR.......")

def registrar_usuario():
    print("======================================")
    print("====== Registro de nueva cuenta ======")
    print("======================================")
    nombre = input("Ingrese su nombre completo: ")
    edad = input("Ingrese su edad: ")
    curp = input("Ingrese su CURP: ").upper()
    telefono = input("Ingrese su telefono: ")

    usuario = input("Defina su nombre de usuario: ")
    contrasenia = input("Defina su contraseña: ")

#Crea el diccionario del nuevo usuario con plan por defecto
    nuevo_usuario = {
        "nombre": nombre,
        "edad": edad,
        "curp": curp,
        "telefono": telefono,
        "usuario": usuario,
        "contrasenia": contrasenia,
        "plan": "Ninguno"
    }

#Añadir usuario a la lista y guardar
    lista_usuarios.append(nuevo_usuario)
    print("\n¡Usuario registrado con exito en el sistema!" )
    print("Regresando al menú principal...")


def mostrar_planes():
    print("\n===============================================================================================================")
    print("|                                     CATÁLOGO DE PLANES                                                      |")
    print("===============================================================================================================")
    print("| 1. Plan Basico  ->  $800.00 MXN / mes                                                                       |")
    print("| INCLUYE: Acceso ilimitado al área de pesas y cardio                                                         |")
    print("|                                                                                                             |")
    print("| 2. Plan Economico ->  $1,000.00 MXN / 2 meses                                                               |")
    print("| INCLUYE: acceso ilimitado a maquinas y uso de regaderas                                                     |")
    print("|                                                                                                             |")
    print("| 3. Plan Premium  ->  $2,500.00 MXN / 6 meses                                                                |")
    print("| INCLUYE: Todo lo anterior + rutina estructurada + asesoría de entrenamiento personalizado                   |")
    print("|                                                                                                             |")
    print("| 2. Plan VIP ->  $4,500.00 MXN / 1 año                                                                       |")
    print("| INCLUYE: Acceso total VIP, plan de nutricion, playera oficial del gym y pase para un invitado gratis al mes |")
    print("===============================================================================================================")
