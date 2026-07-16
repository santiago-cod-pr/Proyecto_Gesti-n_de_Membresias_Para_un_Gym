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
    usuario_ingresado = input("Ingrese su usuario: ")
    contrasenia_ingresada = input("Ingrese su contraseña: ")
    

#PROCEDIMEINTOS 
def mostrar_menu():
    print("*** BIENVENIDO ***")
    print("\n--- Menú principal ---")
    print("1. Registrar nueva cuenta")
    print("2. Iniciar sesión")
    print("3. Ver planes de membresía")
    print("4. Eliminar cuenta")
    print("5. salir")

