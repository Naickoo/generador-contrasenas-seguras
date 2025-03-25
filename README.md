# Generador de Contraseñas Seguras

Este proyecto es un **Gestor de Usuarios y Contraseñas** que permite generar contraseñas seguras, cifrarlas y descifrarlas utilizando claves únicas asociadas a cada usuario. Toda la información se almacena en archivos locales, sin necesidad de usar una base de datos.

## Funcionalidades

- **Registrar usuarios**: Cada usuario tiene una clave de cifrado única.
- **Generar contraseñas seguras**:
  - Contraseñas con letras, números y caracteres especiales.
  - Contraseñas basadas en palabras ingresadas por el usuario.
  - Contraseñas basadas en patrones personalizados.
- **Guardar contraseñas cifradas**: Las contraseñas se cifran con la clave del usuario y se almacenan en un archivo.
- **Descifrar contraseñas**: Descifra contraseñas cifradas utilizando la clave del usuario.
- **Validar contraseñas**: Verifica si una contraseña cumple con criterios de seguridad (longitud mínima, uso de mayúsculas, minúsculas, números y caracteres especiales).

## Requisitos

- **Python 3.7 o superior**
- Biblioteca `cryptography`:
  ```bash
  pip install cryptography
