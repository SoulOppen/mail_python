import re
import os

email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def is_email_valid(email):
    """
    Verifica si un email cumple con la sintaxis del mail.

    Args:
        email (str): El email a verificar.

    Returns:
        bool: True si el email es v lido, False en caso contrario.
    """
    return re.match(email_regex, email) is not None
def archivo_existe(ruta):
    """
    Verifica si un archivo existe en la ruta especificada.

    Args:
        ruta (str): La ruta del archivo a comprobar.

    Returns:
        bool: True si el archivo existe, False en caso contrario.
    """
    return os.path.isfile(ruta)
def execute_python(name):
    """
    Arg:
        name(str) es el nombre del archivo ejecutable.
    Returns:
        int:0 si se ejecuta sin problema.
    """
    return os.system(f"python3 {name}")