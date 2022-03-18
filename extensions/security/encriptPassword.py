from werkzeug.security import generate_password_hash, check_password_hash

def encryptpassw(password):
    texto = password
    textencript = generate_password_hash(texto, 'sha256', 364)
    
    return textencript
    
def desencryptpassw(password, text):
    dato = text
    texto = password
    textdescript = check_password_hash(password, dato)
    return textdescript
