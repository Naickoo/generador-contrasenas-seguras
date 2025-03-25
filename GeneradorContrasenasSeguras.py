import random
import string
import json
from cryptography.fernet import Fernet
from datetime import datetime

# Archivo donde se almacenarán los usuarios y sus claves
ARCHIVO_USUARIOS = "usuarios.json"

def cargar_usuarios():
    """
    Carga los usuarios y sus claves desde el archivo JSON.
    """
    try:
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_usuarios(usuarios):
    """
    Guarda los usuarios y sus claves en el archivo JSON.
    """
    with open(ARCHIVO_USUARIOS, "w") as archivo:
        json.dump(usuarios, archivo)

def registrar_usuario(nombre_usuario):
    """
    Registra un nuevo usuario con una clave de cifrado única.
    """
    usuarios = cargar_usuarios()
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
        return None
    clave = Fernet.generate_key().decode()  # Generar una clave única para el usuario
    usuarios[nombre_usuario] = clave
    guardar_usuarios(usuarios)
    print(f"Usuario '{nombre_usuario}' registrado con éxito.")
    return clave

def obtener_clave_usuario(nombre_usuario):
    """
    Obtiene la clave de cifrado de un usuario.
    """
    usuarios = cargar_usuarios()
    clave = usuarios.get(nombre_usuario)
    if clave is None:
        print("El usuario no existe.")
    return clave

def generar_contrasena(longitud=12, usar_todos=True):
    """
    Genera una contraseña segura con una combinación de caracteres según las preferencias del usuario.
    """
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña debe ser de 8 caracteres.")

    # Conjunto de caracteres según la preferencia del usuario
    if usar_todos:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        caracteres = string.ascii_letters + string.digits

    # Asegurarse de incluir al menos un carácter de cada tipo necesario
    mayuscula = random.choice(string.ascii_uppercase)
    minuscula = random.choice(string.ascii_lowercase)
    numero = random.choice(string.digits)
    especial = random.choice(string.punctuation) if usar_todos else ''

    # Generar el resto de la contraseña
    resto = ''.join(random.choices(caracteres, k=longitud - (4 if usar_todos else 3)))

    # Combinar y mezclar los caracteres
    contrasena = mayuscula + minuscula + numero + (especial if usar_todos else '') + resto
    contrasena = ''.join(random.sample(contrasena, len(contrasena)))

    return contrasena

def generar_contrasena_con_palabras(palabras):
    """
    Genera una contraseña a partir de palabras ingresadas por el usuario, agregando complejidad sin alterar su legibilidad.
    """
    palabras = palabras.replace(" ", "")
    if not palabras:
        raise ValueError("Las palabras no deben estar vacías.")
    
    caracteres_extra = string.digits + string.punctuation + string.ascii_uppercase
    prefijo = ''.join(random.choices(caracteres_extra, k=2))
    sufijo = ''.join(random.choices(caracteres_extra, k=2))

    contrasena = f"{prefijo}{palabras}{sufijo}"
    return contrasena

def generar_contrasena_con_patron(patron):
    """
    Genera una contraseña basada en un patrón definido por el usuario.
    """
    contrasena = ""
    for char in patron:
        if char == "A":
            contrasena += random.choice(string.ascii_uppercase)
        elif char == "a":
            contrasena += random.choice(string.ascii_lowercase)
        elif char == "#":
            contrasena += random.choice(string.digits)
        elif char == "!":
            contrasena += random.choice(string.punctuation)
        else:
            contrasena += char
    return contrasena

def guardar_contrasena(nombre_usuario, contrasena):
    """
    Guarda la contraseña generada cifrada con la clave del usuario.
    """
    clave = obtener_clave_usuario(nombre_usuario)
    if clave is None:
        return
    cifrador = Fernet(clave.encode())
    contrasena_cifrada = cifrador.encrypt(contrasena.encode())
    with open("contrasenas_generadas.txt", "a") as archivo:
        archivo.write(f"{nombre_usuario} - {contrasena_cifrada.decode()}\n")
    print(f"Contraseña guardada para el usuario '{nombre_usuario}'.")

def descifrar_contrasena(nombre_usuario, contrasena_cifrada):
    """
    Descifra una contraseña cifrada usando la clave del usuario.
    """
    clave = obtener_clave_usuario(nombre_usuario)
    if clave is None:
        return
    cifrador = Fernet(clave.encode())
    try:
        contrasena = cifrador.decrypt(contrasena_cifrada.encode()).decode()
        print(f"La contraseña descifrada es: {contrasena}")
    except Exception as e:
        print(f"Error al descifrar la contraseña: {e}")

def validar_contrasena(contrasena):
    """
    Valida si una contraseña cumple con los criterios de seguridad.
    """
    if len(contrasena) < 8:
        return False
    if not any(char.isupper() for char in contrasena):
        return False
    if not any(char.islower() for char in contrasena):
        return False
    if not any(char.isdigit() for char in contrasena):
        return False
    if not any(char in string.punctuation for char in contrasena):
        return False
    return True

def menu():
    """
    Muestra un menú interactivo para gestionar usuarios y contraseñas.
    """
    while True:
        print("\n--- Gestor de Usuarios y Contraseñas ---")
        print("1. Registrar un nuevo usuario")
        print("2. Generar y guardar una contraseña")
        print("3. Descifrar una contraseña")
        print("4. Validar una contraseña")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_usuario = input("Introduce el nombre del usuario: ")
            registrar_usuario(nombre_usuario)
        elif opcion == "2":
            nombre_usuario = input("Introduce el nombre del usuario: ")
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8 caracteres): "))
            usar_todos = input("¿Usar todos los caracteres (S/N)? ").strip().lower() == "s"
            contrasena = generar_contrasena(longitud, usar_todos)
            print(f"Tu contraseña segura es: {contrasena}")
            guardar_contrasena(nombre_usuario, contrasena)
        elif opcion == "3":
            nombre_usuario = input("Introduce el nombre del usuario: ")
            contrasena_cifrada = input("Introduce la contraseña cifrada: ")
            descifrar_contrasena(nombre_usuario, contrasena_cifrada)
        elif opcion == "4":
            contrasena = input("Introduce la contraseña a validar: ")
            if validar_contrasena(contrasena):
                print("La contraseña es segura.")
            else:
                print("La contraseña no cumple con los criterios de seguridad.")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()