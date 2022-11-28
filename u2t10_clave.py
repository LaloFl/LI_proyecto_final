def main():
    _usuario = "admin"
    _clave = "admin"
    acceso = False
    while not acceso:
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        if usuario == _usuario and clave == _clave:
            acceso = True
        else:
            print("Acceso denegado")
            
    print("Acceso concedido")
