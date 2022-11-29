from app import auth

from . import auth_bp as bp

from werkzeug.security import generate_password_hash, check_password_hash

@auth.verify_password
def verify_password(username, password):
    # PARA FINES DE PRUEBAS
    _password = generate_password_hash("holamundo")
    _username = "admin"

    if (username.lower() == _username.lower()) and (check_password_hash(_password, password)):
        return True

    return False
