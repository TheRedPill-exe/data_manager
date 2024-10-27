import tkinter as tk
from tkinter import messagebox
from src.user_manager import add_user, update_user_field, delete_user, show_data, load_users

class UserManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("User Manager")

        # Botones para las diferentes acciones
        tk.Button(master, text="Agregar Usuario", command=self.add_user_window).pack()
        tk.Button(master, text="Actualizar Usuario", command=self.update_user_window).pack()
        tk.Button(master, text="Eliminar Usuario", command=self.delete_user_window).pack()
        tk.Button(master, text="Mostrar Usuarios", command=self.show_data_window).pack()

    def add_user_window(self):
        # Ventana para agregar usuario
        window = tk.Toplevel(self.master)
        window.title("Agregar Usuario")

        tk.Label(window, text="ID:").pack()
        user_id_entry = tk.Entry(window)
        user_id_entry.pack()

        tk.Label(window, text="Nombre:").pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="Email:").pack()
        email_entry = tk.Entry(window)
        email_entry.pack()

        tk.Label(window, text="Fecha de Nacimiento:").pack()
        birth_date_entry = tk.Entry(window)
        birth_date_entry.pack()

        def add_user_action():
            user_id = user_id_entry.get()
            name = name_entry.get()
            email = email_entry.get()
            birth_date = birth_date_entry.get()

            user_data = {
                "id": user_id,
                "name": name,
                "email": email,
                "birth_date": birth_date
            }

            if add_user(user_data):
                messagebox.showinfo("Éxito", "Usuario agregado exitosamente.")
                window.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar el usuario.")

        tk.Button(window, text="Agregar", command=add_user_action).pack()

    def update_user_window(self):
        # Ventana para actualizar usuario
        window = tk.Toplevel(self.master)
        window.title("Actualizar Usuario")

        tk.Label(window, text="Campo a Actualizar (id, name, email, birth_date):").pack()
        field_entry = tk.Entry(window)
        field_entry.pack()

        tk.Label(window, text="Valor Actual:").pack()
        current_value_entry = tk.Entry(window)
        current_value_entry.pack()

        tk.Label(window, text="Nuevo Valor:").pack()
        new_value_entry = tk.Entry(window)
        new_value_entry.pack()

        def update_user_action():
            field = field_entry.get()
            current_value = current_value_entry.get()
            new_value = new_value_entry.get()

            # Llamar a la función para actualizar el campo del usuario
            update_user_field(field, current_value, new_value, "data/users.json")
            messagebox.showinfo("Éxito", "Usuario actualizado exitosamente.")
            window.destroy()

        tk.Button(window, text="Actualizar", command=update_user_action).pack()

    def delete_user_window(self):
        # Ventana para eliminar usuario
        window = tk.Toplevel(self.master)
        window.title("Eliminar Usuario")

        tk.Label(window, text="ID del Usuario a Eliminar:").pack()
        user_id_entry = tk.Entry(window)
        user_id_entry.pack()

        def delete_user_action():
            user_id = user_id_entry.get()
            delete_user(user_id, "data/users.json")
            messagebox.showinfo("Éxito", "Usuario eliminado exitosamente.")
            window.destroy()

        tk.Button(window, text="Eliminar", command=delete_user_action).pack()

    def show_data_window(self):
        # Ventana para mostrar los usuarios
        window = tk.Toplevel(self.master)
        window.title("Mostrar Usuarios")

        tk.Label(window, text="Campo para Buscar (id, name, email, birth_date):").pack()
        field_entry = tk.Entry(window)
        field_entry.pack()

        tk.Label(window, text="Valor a Buscar:").pack()
        value_entry = tk.Entry(window)
        value_entry.pack()

        def show_data_action():
            field = field_entry.get()
            value = value_entry.get()
            output = show_data(field, value, "data/users.json")
            
            # Crear una ventana para mostrar los resultados
            result_window = tk.Toplevel(window)
            result_window.title("Resultados")
            if output:
                tk.Label(result_window, text=output).pack()
            else:
                tk.Label(result_window, text="No se encontraron resultados.").pack()

        tk.Button(window, text="Mostrar", command=show_data_action).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagerApp(root)
    root.mainloop()
