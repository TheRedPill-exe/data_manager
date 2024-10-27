import re
def validate(user):
    if not user.get("id"):
        return False  # ID debe estar presente y no puede ser vacío
    
    if not user.get("name"):
        return False  # Nombre debe estar presente y no puede ser vacío
    
    if not user.get("email") or not re.match(r"[^@]+@[^@]+\.[^@]+", user["email"]):
        return False  # Correo debe estar presente y ser válido
    
    if not user.get("birth_date"):
        return False  # Fecha de nacimiento debe estar presente y no puede ser vacío

    # Si todas las validaciones pasan, retornamos True
    return True