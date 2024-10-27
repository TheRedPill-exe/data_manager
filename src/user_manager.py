from src.validation import validate
from .file_handler import load_users, save_update, filename

def find_data(field, data_to_find, users):
    for user in users:
        if user.get(field) == data_to_find:
            return True
    return False

def update_user_field(field, data, new_data, filename=filename):
    users = load_users(filename)
    
    try:
        if find_data(field, data, users):
            for user in users:
                if user.get(field) == data:
                    print(f"{field} from the user {user[field]} changed to {new_data}.")
                    user[field] = new_data
                    if validate(user):
                        save_update(users)
                    else:
                        print("User data is invalid. Changes were not saved.")
                    return
            print(f"{field} {data} not found.")
    except:
        print("Unexpected error")

def show_data(field, data_to_find, filename=filename):
    users = load_users()
    if find_data(field, data_to_find, users):
        for user in users:
            if user[field] == data_to_find:
                output = "\n".join(f"{key}: {value}" for key, value in user.items())
                print(output)
                return output  # Asegúrate de retornar la salida
    else:
        print(f"{field} '{data_to_find}' not found.")

def add_user(new_user):
    users = load_users(filename)
    
    if validate(new_user):
        users.append(new_user)
        save_update(users, filename)
        print("User added successfully.")
        return True
    else:
        print("User data is invalid. User was not added.")


def delete_user(user_id, filename=filename):
    users = load_users(filename)
    if find_data("id", user_id, users):
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                save_update(users)  # Asegúrate de que esto se ejecute
                print(f"User with id {user_id} deleted.")
                return
    else:
        print("User not found.")

