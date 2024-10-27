import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Directorio raíz del proyecto
filename = os.path.join(BASE_DIR, "data", "users.json")

def load_users(filename=filename):
    """Carga los datos de usuarios desde el archivo JSON."""
    try:
        with open(filename, "r") as jusers:
            return json.load(jusers)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar el archivo JSON.")
        return []
    
def save_update(users,filename=filename):
    try:
        with open(filename, "w") as jusers:
            json.dump(users, jusers, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al sobrescribir los datos")


