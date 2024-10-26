import json

with open("data/users.json","r") as jusers:
    users = json.load(jusers)

def update_user(username, newusername):
    for user in users:
        if user.name == username:
            user.name = newusername
            break

    print("Usuario no encontrado")
update_user("Juan","pablo")