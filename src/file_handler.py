import json

def load_users(filename="data/users.json"):
    """Carga los datos de usuarios desde el archivo JSON."""
    try:
        with open(filename, "r") as jusers:
            return json.load(jusers)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar el archivo JSON.")
        return []
    
def save_update(users,filename="data/users.json"):
    try:
        with open(filename, "w") as jusers:
            json.dump(users, jusers, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al sobrescribit los datos")

def find_data(field, data_to_find, users):
    for user in users:
        if user.get(field) == data_to_find:
            return True
    return False

def update_username(field,new_data,filename="data/users.json"):
    users = load_users()

    try:
        if(find_data(user_name)):
            for user in users:
                if user.get

    


