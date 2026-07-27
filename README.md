# Proyecto_Gesti-n_de_Membresias_Para_un_Gym
Repositorio Para Trabajar en Equipo para el desarrollo de un Sistema para la Gestión de membresias en un Gimnasio.

README — Sistema de Gestión de Membresías  

Descripción General del Proyecto: 

El Sistema de Gestión de Membresías para Gimnasio es una aplicación interactiva en consola diseñada para administrar el registro de usuarios, la selección y compra de planes de entrenamiento, el procesamiento simulado de pagos con tarjeta de crédito/débito y la emisión de tickets. Además, incluye persistencia de datos mediante archivos CSV, asegurando que la información de los usuarios y compras se conserve permanentemente tras la ejecución. 

Instrucciones de Ejecución: 

Siga estos pasos para ejecutar la aplicación correctamente en su entorno local: 

Asegúrese de tener instalado Python  

Guarde el archivo con el código fuente 

Abrir la consola 

Iniciar comando de ejecucion

Descripción Breve de las Funciones del Código: 

 

cargar_usuarios(): Esta función verifica si existe el archivo local "usuarios.csv" en el sistema. En caso de encontrarlo, lee y procesa cada fila del archivo para transformar la información guardada en una lista global de diccionarios al iniciar el programa; si no existe, retorna una lista vacía de forma segura. 

guardar_usuarios(): Esta función se encarga de la persistencia de datos escribiendo la lista global de usuarios en el archivo "usuarios.csv". Formatea la información con los encabezados correspondientes (nombre, edad, CURP, teléfono, usuario, contraseña, plan y tarjeta) asegurando que los cambios de registro, compras o eliminaciones queden guardados permanentemente. 

buscar_usuario(usuario_ingresado, contrasenia_ingresada): Esta función recorre la lista global de usuarios registrados para verificar si coinciden las credenciales de usuario y contraseña recibidas como argumentos. Retorna el diccionario completo con los datos del usuario si se encuentra una coincidencia exacta; de lo contrario, devuelve None. 

mostrar_planes(): Esta función despliega en pantalla el catálogo visual de las membresías disponibles con sus precios y beneficios detallados. Valida la selección del plan (1 al 4), gestiona la autenticación obligatoria antes de la compra, solicita y valida los datos bancarios de pago y actualiza la membresía contratada en el perfil del usuario activo antes de generar su ticket. 

iniciar_sesion(): Esta función solicita las credenciales al usuario e invoca a buscar_usuario para validar el acceso al sistema. Si la autenticación es exitosa, establece la sesión activa, muestra un mensaje personalizado con distinción para miembros especiales (planes Premium o VIP) y retorna True; en caso de error, ofrece una opción recursiva para reintentar e informa del fallo devolviendo False. 

mostrar_menu(): Este procedimiento imprime en consola la interfaz visual del menú principal con un encabezado decorativo y la lista numerada de opciones disponibles. Utiliza las constantes definidas en el programa para presentar un menú claro, limpio y estructurado que guía al usuario durante toda la interacción. 

registrar_usuario(): Este procedimiento gestiona la creación e incorporación de nuevas cuentas al sistema capturando datos como nombre, edad, CURP, teléfono, usuario y contraseña. Incluye validaciones estrictas para asegurar que el usuario sea mayor de edad (18+ años), que la CURP contenga 18 caracteres, que el teléfono tenga 10 dígitos y que el nombre de usuario no esté duplicado, asignando la cuenta registrada como la sesión activa. 

eliminar_cuenta(): Este procedimiento permite dar de baja a un usuario registrado solicitando previamente la confirmación de sus credenciales por seguridad. Una vez autenticado el usuario, requiere una confirmación explícita (SI/NO) antes de remover permanentemente el registro de la lista del sistema, incluyendo una rutina de reintento en caso de proporcionar datos erróneos. 

ver_usuarios_registrados(): Este procedimiento genera un reporte impreso formateado en forma de tabla con todos los clientes almacenados en el sistema. Muestra detalladamente campos clave como nombre completo, edad, CURP, teléfono, usuario y el plan de membresía asignado actualmente, informando adecuadamente si la base de datos se encuentra vacía. 

imprimir_ticket(): Este procedimiento emite un comprobante formal de la transacción en formato de recibo tras la contratación exitosa de una membresía. Recupera la información de la sesión activa para mostrar en pantalla el nombre del cliente, su CURP, el plan adquirido y la confirmación del pago aprobado. 

ejecutar_menu(): Esta función actúa como el bucle ejecutor y controlador principal del ciclo de vida del programa. Muestra continuamente el menú, captura la opción seleccionada por el usuario, maneja excepciones de entrada para evitar fallos inesperados y redirige el flujo de ejecución hacia la función o procedimiento correspondiente hasta seleccionar la opción de salir. 

