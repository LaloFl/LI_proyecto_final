def main():
    def cantidad_vocales(cadena): 
        cant=0 
        for x in range(len(cadena)): 
            if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u": 
                cant=cant+1 
        print("Cantidad de vocales de la palabra" , cadena, "es", cant) 

    def cantidad_vocales_y_letras(cadena): 
        cant=0 
        for x in range(len(cadena)): 
            if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u": 
                cant=cant+1 
        print(f"La palabra \"{cadena}\" tiene {len(cadena)} caracteres y {cant} vocales") 

    def tipo_triangulo(*args): 
        a=args[0] 
        b=args[1] 
        c=args[2] 
        tipo = "" 
        tipo = "Equilátero" if (a == b and b == c) else "Isóceles" if (a == b or b == c or a == c) else "Escaleno" 
        print(f"El triángulo con lados {args} es {tipo}")

    # cantidad_vocales() 
    cantidad_vocales("administracion") 
    cantidad_vocales("hola mundo") 
    cantidad_vocales("ana") 
    # cantidad_vocales_y_letras() 
    cantidad_vocales_y_letras("hola soy Diego") 
    cantidad_vocales_y_letras("pruebas") 
    cantidad_vocales_y_letras("hola hola") 
    cantidad_vocales_y_letras("hola me llamo Diego Flores") 
    # tipo_triangulo() 
    tipo_triangulo(2, 2, 2) #Equilátero 
    tipo_triangulo(2, 2, 1) #Isóceles 
    tipo_triangulo(3, 2, 1) #Escaleno