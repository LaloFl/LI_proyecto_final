from imports import *

def main():
    clear()
    # _username = "1"
    # _password = "1"
    # correct_credentials = False
    # while not correct_credentials:
    #     username = input("Usuario: ")
    #     password = input("Contraseña: ")
    #     if username != _username:
    #         print("Usuario incorrecto")
    #     if password != _password:
    #         print("Contraseña incorrecta")  
    #     elif username == _username:
    #         correct_credentials = True
    return menu()

def menu():
    clear()
    print("Bienvenido")
    for practica in practicas:
        print(f"{practicas.index(practica) + 1}. {practica['nombre']}")
    print("0. Salir")

    practica = input("Elige una práctica: ")
    if practica == "0":
        return my_exit()
    clear()
    try:
        practica_seleccionada = practicas[int(practica) - 1]
        print(f"-------------------------------- {practica_seleccionada['nombre'].upper()} --------------------------------")
        practica_seleccionada["funcion"]()
        return sub_menu(practica_seleccionada)
    except:
        return menu()

def sub_menu(practica):
    print("\n-------------------------------- SUB MENÚ --------------------------------")
    print("1. Regresar al menú principal")
    print("2. Repetir práctica")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        return menu()
    elif opcion == "2":
        clear()
        print(f"-------------------------------- {practica['nombre'].upper()} --------------------------------")
        practica["funcion"]()
        return sub_menu(practica)
    elif opcion == "3":
        return my_exit()
    else:
        return sub_menu(practica)
    
if __name__ == "__main__":
    main()