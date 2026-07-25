# Equipo 6 - SISTEMA DE GESTION DE MEMBRESIAS PARA UN GYM.

#CONSTANTES PARA LAS OPCIONES DEL MENÚ
OPCION_NUEVA_CUENTA = 1
OPCION_INICIAR_SESION = 2
OPCION_VER_PLANES = 3
OPCION_ELIMINAR_CUENTA = 4
OPCION_VER_USUARIOS = 5
OPCION_SALIR = 6

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
    #leer plan seleccionado 
    plan_opcion = input ("\nSeleccione el plan que desea adquirir (1-4): ")

    #verificar si hay alguien con sesion activa
    if sesion_activa is None:
        print("\nPara contratar un plan debes ingresar a tu cuenta.")
        login_exitoso = iniciar_sesion()

        #si la persona no tiene una cuenta
        if not login_exitoso:
            print("\nNo se pudo verificar tu cuenta.")
            crear = input("¿Desea crear una cuenta nueva? (si/no): ")
            if crear == "si":
                registrar_usuario()
            return #corta el proceso para que no se pueda pagar sin cuenta

    #datos de pago 
    print("\n--- Datos de pago ---")
    tarjeta = input("Ingrese numero de tarjeta: ")
    cvv = input("Ingrese CVV: ")
    fecha = input("Ingrese fecha de vencimiento (MM/AA): ")

    #Guardar el plan contratado en el usuario
    if plan_opcion == "1":
        sesion_activa["plan"] = "Basico"
    elif plan_opcion == "2":
            sesion_activa["plan"] = "Economico"
    elif plan_opcion == "3":
            sesion_activa["plan"] = "Premium"
    elif plan_opcion == "4":
            sesion_activa["plan"] = "VIP"

    imprimir_ticket()


def iniciar_sesion():
    global sesion_activa
    print("\n --- INICIO DE SESIÓN ---")
    usuario = input("Ingrese su usuario: ")
    contrasenia = input("Ingrese su contraseña: ")

    usuario_encontrado = buscar_usuario(usuario, contrasenia)
    
    if usuario_encontrado is not None:
        sesion_activa = usuario_encontrado
        print(f"\n¡Inicio de sesión exitoso! Bienvenido {sesion_activa['nombre']}.")
        #Evalua si es miembro especial
        if sesion_activa["plan"] in ["Premium", "VIP"]:
            print("¡Bienvenido miembro especial! 👑")

        print(f"Resumen de cuenta -> Plan actual: {sesion_activa['plan']}")
        return True
    else:
        print("\nError usuario o contraseña incorrectos.")

        reintentar = input("¿Desea reintentar? (si/no): ")
        if reintentar == "si": 
            return iniciar_sesion() #Vuelve a llamarse a sí misma para reintentar
        return False



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
    print(f"{OPCION_VER_USUARIOS}. Ver usuarios registrados")
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



#Procedimiento Para eliminar cuenta
def eliminar_cuenta():
    print("==================================================")
    print("======          ELIMINAR CUENTA          =========")
    print("==================================================")
    
    usuario = input("Ingrese su Usuario: ")
    contrasenia = input("Ingrese su contraseña: ")

    usuario_encontrado = buscar_usuario(usuario, contrasenia)

    if usuario_encontrado is not None:
        confirmacion = input(f"Seguro que desea eliminar la cuenta de {usuario_encontrado['nombre']}? (SI/NO: )").strip().upper()
        if confirmacion == "SI":
            lista_usuarios.remove(usuario_encontrado)
            print("!! CUENTA ELIMINADA CON EXITO !!")
        else:
            print("\n OPERACION CANCELADA. LA CUENTA NO FUE ELIMINADA.")
    else:
        print("\n!!! ERROR: Inexistente o Datos Incorrectos")
        # Punto para reintentar
        reintentar = input("¿Desea reintentar? (SI/NO): ").strip().upper()
        if reintentar == "SI":
            eliminar_cuenta() # Se vuelve a llamar


# Procedimiemto: Usuarios Registrados.

def ver_usuarios_registrados():
    print("\n====================================================================================")
    print("=======                 REPORTE: USUARIOS REGISTRADOS                        =======")
    print("====================================================================================")
    
    if not lista_usuarios:
        print("No hay usuarios registrados en el sistema actualmente.")
        print("====================================================================================")
        return

    print(f"{'Nombre':<25} | {'Edad':<4} | {'CURP':<12} | {'Teléfono':<11} | {'Usuario':<12} | {'Plan':<10}")
    print("-" * 84)
    for u in lista_usuarios:
        print(f"{u['nombre']:<25} | {u['edad']:<4} | {u['curp']:<12} | {u['telefono']:<11} | {u['usuario']:<12} | {u['plan']:<10}")
    print("====================================================================================")

# Procedimiento para imprimir ticket
def imprimir_ticket():
    global sesion_activa
    print("\n=================================")
    print("        TICKET DE COMPRA         ")
    print("=================================")
    print(f"Cliente: {sesion_activa['nombre']}")
    print(f"CURP: {sesion_activa['curp']}")
    print(f"Plan contratado: {sesion_activa['plan']}")
    print("Estado del pago: APROBADO EXITOSAMENTE")
    print("=================================\n")



def ejecutar_menu():
    while True:
        mostrar_menu()  # Muestra las opciones visuales en pantalla
        
        try:
            opcion = int(input("-> Opción: "))
            
            if opcion == OPCION_NUEVA_CUENTA:
                registrar_usuario()
            elif opcion == OPCION_INICIAR_SESION:
                iniciar_sesion()
            elif opcion == OPCION_VER_PLANES:
                mostrar_planes()
            elif opcion == OPCION_ELIMINAR_CUENTA:
                eliminar_cuenta()
            elif opcion == OPCION_VER_USUARIOS:
                ver_usuarios_registrados()
            elif opcion == OPCION_SALIR:
                print("\n¡Gracias por usar nuestro sistema! Hasta luego. 💪")
                break  # Rompe el ciclo 'while True' de forma segura
            else:
                print("\nOpción inválida. Intente de nuevo.")
                
        except ValueError:
            print("\nError: Por favor, ingrese un número válido (caracteres no permitidos).")


# INICIALIZACIÓN DE ARRANQUE 
ejecutar_menu()