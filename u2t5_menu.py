from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def main():
    opc = -1

    texto = "¡Morir es nada cuando por la patria se muere!"+"\n\nJosé María Morelos y Pavón"+"\n\n\n\tLa madrugada del 16 de septiembre de 1810, El cura Don "+"\n"+"Miguel Hidalgo y Costilla convocó al pueblo de Dolores Hidalgo, a "+"\n"+"través del repique de las campanas de su iglesia, a levantarse en "+"\n"+"armas en contra del dominio de los españoles."+"\n\nEl periodo de nuestra historia conocido como la Guerra de "+"\n"+"Independencia empieza (estrictamente hablando) la madrugada "+"\n"+"del 16 de septiembre de 1810, cuando el padre Miguel Hidalgo da el "+"\n"+"llamado ‘Grito de Dolores’ y termina el 27 de septiembre de 1821 (11 "+"\n"+"años después) con la entrada triunfal del Ejército Trigarante, "+"\n"+"encabezado por Agustín de Iturbide y Vicente Guerrero, a una "+"\n"+"jubilosa Ciudad de México. El objetivo principal de este "+"\n"+"movimiento (armado y social) era liberar a nuestro territorio del "+"\n"+"yugo español y que, en cada rincón de la Colonia se olvidase "+"\n"+"por completo el concepto de virreinato."

    def minimenu(cb):
        opc = input("\nRepetir (1). Regresar a menú (2): ")
        if opc == "1":
            cb()

    def opc1():
        clear()
        print(texto)
        minimenu(opc1)

    def opc2():
        clear()
        print("SUMA (a + b)")
        sum_a = float(input("a) Ingresa un número: "))
        sum_b = float(input("b) Ingresa un número: "))
        sum_r = sum_a + sum_b
        print(f"{sum_a} + {sum_b} = {sum_r}\n")
        print("RESTA (a - b)")
        resta_a = float(input("a) Ingresa un número: "))
        resta_b = float(input("b) Ingresa un número: "))
        resta_r = resta_a - resta_b
        print(f"{resta_a} - {resta_b} = {resta_r}\n")
        print("MULTIPLICACIÓN (a * b)")
        mul_a = float(input("a) Ingresa un número: "))
        mul_b = float(input("b) Ingresa un número: "))
        mul_r = mul_a * mul_b
        print(f"{mul_a} * {mul_b} = {mul_r}\n")
        print("DIVISIÓN (a / b)")
        div_a = float(input("a) Ingresa un número: "))
        div_b = float(input("b) Ingresa un número: "))
        div_r = div_a / div_b
        print(f"{div_a} / {div_b} = {div_r}\n")
        minimenu(opc2)

    def opc3():
        clear()
        preg_1 = input("1. ¿Cuál es tu primer nombre?: ")
        preg_2 = input("2. ¿Cuál es tu apellido paterno?: ")
        preg_3 = input("3. ¿Cuál es tu apellido materno?: ")
        preg_4 = input("4. ¿Qué edad tienes?: ")
        preg_5 = input("5. ¿Qué carrera estudias?: ")
        preg_6 = input("6. ¿En qué semestre cursas?: ")

        print(f"\n\n1. Tu primer nombre es {preg_1}")
        print(f"2. Tu apellido paterno es {preg_2}")
        print(f"3. Tu apellido materno es {preg_3}")
        print(f"4. Tienes {preg_4} años")
        print(f"5. Estudias la carrera de {preg_5}")
        print(f"6. Cursas el semestre número {preg_6}")
        minimenu(opc3)

    while opc != "4":
        clear()
        print("--------------MENÚ--------------")
        print("1. Texto (párrafos).")
        print("2. Operaciones aritméticas.")
        print("3. 6 preguntas.")
        print("4. Salir del programa.")
        opc = input("\nSelecciona una opción del menú: ")

        if opc == "1":
            opc1()
        elif opc == "2":
            opc2()
        elif opc == "3":
            opc3()

