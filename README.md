# 🔒 Generador de Contraseñas Seguras

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python) 
![Cryptography](https://img.shields.io/badge/Cryptography-Fernet-green)

Un **gestor de contraseñas seguro y local** que cifra tus credenciales con claves únicas. ¡Sin bases de datos, sin nube, solo archivos en tu máquina! 🚀

## ✨ Funcionalidades destacadas

| Característica | Descripción |
|---------------|-------------|
| 🔐 **Registro seguro** | Cada usuario tiene su propia clave de cifrado AES-256 |
| � **Generación inteligente** | Opciones flexibles: aleatorias, basadas en palabras o patrones |
| 🏦 **Almacenamiento cifrado** | Tus contraseñas se guardan con cifrado Fernet |
| 🔍 **Recuperación fácil** | Descifrado rápido con tu clave personal |
| 🛡️ **Validador integrado** | Verifica fortaleza de contraseñas al instante |

## 📦 Requisitos e instalación

# 1. Clona el repositorio
- `git clone https://github.com/Naickoo/generador-contrasenas-seguras.git`
- `cd generador-contrasenas-seguras`

# 2. Instala dependencias
`pip install cryptography`


---

## 📂 Archivos generados  

| Archivo                     | Descripción                     |
|-----------------------------|---------------------------------|
| `usuarios.json`             | Usuarios y claves de cifrado    |
| `contrasenas_generadas.txt` | Contraseñas cifradas           |

---

## 🚀 Cómo usarlo  

1. Clona el repositorio:
    - `git clone https://github.com/Naickoo/generador-contrasenas-seguras.git`
    - `cd generador-contrasenas-seguras`
   
2. Ejecuta el programa:
   - `python GeneradorContrasenasSeguras.py`
   
3. Sigue el menú interactivo para:  
- Registrar usuarios  
- Generar/guardar contraseñas  
- Descifrar contraseñas  
- Validar fortaleza 

---

## 📋 Ejemplo de uso  

**Registro de usuario**:  
- Introduce el nombre del usuario: usuario1
- Usuario 'usuario1' registrado con éxito.

**Generar contraseña**:  
- Longitud de la contraseña (mínimo 8): 12
- ¿Usar todos los caracteres? (S/N): S
- Tu contraseña segura es: A1!b2@c3#d4

**Descifrar contraseña**:  
- Usuario: usuario1
- Contraseña cifrada: gAAAAABk...
- La contraseña descifrada es: A1!b2@c3#d4


---

## 🤝 Contribuciones  

¡Bienvenidas las contribuciones! Puedes:  
- Reportar errores en Issues  
- Proponer mejoras mediante Pull Requests  

---
