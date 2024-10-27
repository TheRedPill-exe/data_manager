# User Management System

Este proyecto es un sistema de gestión de usuarios que permite agregar, actualizar, eliminar y mostrar información de usuarios a través de una interfaz gráfica de usuario (GUI) desarrollada en Python utilizando la biblioteca Tkinter. Los datos de los usuarios se almacenan en un archivo JSON, lo que permite una fácil manipulación y persistencia de la información.
## Despliegue: https://drive.google.com/file/d/1z8suVDkeVA2p8HFNAw-B05X407xn7v5a/view?usp=sharing
## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura de Archivos](#estructura-de-archivos)
- [Instrucciones de Instalación](#instrucciones-de-instalación)
- [Uso](#uso)


## Descripción del Proyecto

El sistema permite a los usuarios realizar las siguientes acciones:

- **Agregar un nuevo usuario**: Introducir datos como ID, nombre, correo electrónico y fecha de nacimiento.
- **Actualizar información de un usuario**: Modificar campos específicos de los usuarios existentes.
- **Eliminar un usuario**: Eliminar un usuario del sistema mediante su ID.
- **Mostrar información de los usuarios**: Buscar y mostrar detalles de los usuarios.

## Características

- Interfaz gráfica intuitiva y fácil de usar.
- Validación de datos para asegurar que la información ingresada sea correcta.
- Almacenamiento persistente de datos utilizando JSON.
- Soporte para múltiples operaciones de gestión de usuarios.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo.
- **Tkinter**: Biblioteca para crear la interfaz gráfica de usuario.
- **JSON**: Formato de datos utilizado para el almacenamiento de usuarios.
- **Pip**: Para la gestión de dependencias (tkinter).
## Arquitectura
data_manager/ <br>
├── data/ <br>
│   └── users.json  <br>
├── src/ <br>
│   ├── __init__.py <br>
│   ├── file_handler.py  <br>
│   ├── menu.py <br>
│   ├── user_manager.py  <br>
│   └── validation.py  <br>
└── tests/ <br>
    └── test_user_manager.py

## Instrucciones de Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/TheRedPill-exe/data_manager

