## Instalación

Para ejecutar este proyecto correctamente, es necesario instalar algunas dependencias y configurar el entorno adecuadamente. Esto garantiza que todas las librerías y herramientas que utiliza el código estén disponibles y funcionen sin problemas.

Este proyecto utiliza Python y requiere la instalación de paquetes específicos para manejar archivos Excel, enviar correos electrónicos mediante Outlook y manipular datos fácilmente. Además, es recomendable crear un ambiente virtual para aislar las dependencias y evitar conflictos con otras aplicaciones en tu sistema.

A continuación, se detallan los pasos para preparar el entorno de trabajo y asegurarte de que todo esté listo para ejecutar el proyecto.

### Crear y activar un ambiente virtual

1. Abre una terminal y navega a la carpeta raíz del proyecto.

2. Ejecuta el siguiente comando para crear un ambiente virtual llamado `env`:

```bash
python -m venv env
```
3. Activa el ambiente virtual:

- En Windows (CMD o PowerShell):

```bash
env\Scripts\activate

- En mac o linux(wsl):

```bash
source env/bin/activate

```bash
pip install -r requirements.txt
