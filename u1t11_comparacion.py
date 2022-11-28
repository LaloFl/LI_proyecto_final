def main():
    a = int(input("Ingresa un número (a): "))
    b = int(input("Ingresa un número (b): "))

    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} es igual a {b}")
