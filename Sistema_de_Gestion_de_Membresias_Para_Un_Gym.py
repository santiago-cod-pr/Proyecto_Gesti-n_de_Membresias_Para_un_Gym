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
def iniciar_sesion():
    print("\n --- INICIO DE SESIÓN ---")
    usuario = input("Ingrese su usuario: ")
    contrasenia = input("Ingrese su contraseña: ")


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
