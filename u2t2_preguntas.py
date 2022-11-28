def main():
    preguntas = [
        "Cuál es tu nombre", 
        "Cuál es tu edad",
        "Cuál es tu sexo",
        "Cuál es tu estado civil",
        "Cuál es tu ocupación",
        "Cuál es tu deporte favorito",
        "Porcentaje de nivel de ingles",
        "En qué escuela estudias",
        "Qué carrera estudias",
        "Cuál es tu promedio",
    ]
    respuestas = []

    for pregunta in preguntas:
        respuestas.append(input(pregunta + ": "))
    
    print("\nRespuestas:")
    for pregunta in preguntas:
        print(f"{pregunta}: {respuestas[preguntas.index(pregunta)]}")