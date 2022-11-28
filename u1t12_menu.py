from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def main():
    def menu():
        print("Menú")
        print("1. Suma")
        print("2. Resta")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        clear()

        if opcion == "3":
            return
        elif opcion == "1":
            return suma()
        elif opcion == "2":
            return resta()
        else:
            return menu()

    def submenu(action):
        print("Submenú")
        print("1. Regresar al menú principal")
        print("2. Repetir operación")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        clear()

        if opcion == "1":
            return menu()
        elif opcion == "2":
            return submenu(action)
        elif opcion == "3":
            return

    def suma():
        print("Suma")
        a = int(input("Ingresa un número (a): "))
        b = int(input("Ingresa un número (b): "))
        print(f"Resultado: {a + b}")
        return submenu(suma)

    def resta():
        print("Resta")
        a = int(input("Ingresa un número (a): "))
        b = int(input("Ingresa un número (b): "))
        print(f"Resultado: {a - b}")
        return submenu(resta)

    return menu()

