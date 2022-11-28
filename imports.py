from os import system, name
from threading import enumerate

# PRÁCTICAS
# U1
from u1t1_portada import main as u1t1
from u1t2_cadenas import main as u1t2
from u1t3_cuestionario import main as u1t3
from u1t4_pregunta import main as u1t4
from u1t5_boleta import main as u1t5
from u1t6_cuadrado import main as u1t6
from u1t7_4num import main as u1t7
from u1t8_unidades import main as u1t8
from u1t9_operaciones import main as u1t9
from u1t11_comparacion import main as u1t11
from u1t12_menu import main as u1t12
# U2
from u2t1_portada import main as u2t1
from u2t2_preguntas import main as u2t2
from u2t3_menu import main as u2t3
from u2t4_boleta import main as u2t4
from u2t6_ciclos import main as u2t6
from u2t8_tablas import main as u2t8
from u2t10_clave import main as u2t10
from u2t14_triangulos import main as u2t14
from u2t15_calculadora import main as u2t15


def clear():
    system('cls' if name == 'nt' else 'clear')

def my_exit():
    clear()
    for thread in enumerate():
        if thread.name != "MainThread":
            thread.join()

practicas = [
    {
        "nombre": "U1T1. Portada",
        "funcion": u1t1
    },
    {
        "nombre": "U1T2. Cadenas",
        "funcion": u1t2
    },
    {
        "nombre": "U1T3. Cuestionario",
        "funcion": u1t3
    },
    {
        "nombre": "U1T4. Pregunta",
        "funcion": u1t4
    },
    {
        "nombre": "U1T5. Boleta",
        "funcion": u1t5
    },
    {
        "nombre": "U1T6. Cuadrado",
        "funcion": u1t6
    },
    {
        "nombre": "U1T7. Captura de 4 números",
        "funcion": u1t7
    },
    {
        "nombre": "U1T8. Sistema de unidades",
        "funcion": u1t8
    },
    {
        "nombre": "U1T9. Operaciones",
        "funcion": u1t9
    },
    {
        "nombre": "U1T11. Comparación",
        "funcion": u1t11
    },
    {
        "nombre": "U1T12. Menú",
        "funcion": u1t12
    },
    {
        "nombre": "U2T1. Portada",
        "funcion": u2t1
    },
    {
        "nombre": "U2T2. Preguntas",
        "funcion": u2t2
    },
    {
        "nombre": "U2T3. Menú",
        "funcion": u2t3
    },
    {
        "nombre": "U2T4. Boleta",
        "funcion": u2t4
    },
    {
        "nombre": "U2T6. Ciclos",
        "funcion": u2t6
    },
    {
        "nombre": "U2T8. Tablas de multiplicación",
        "funcion": u2t8
    },
    {
        "nombre": "U2T10. Clave",
        "funcion": u2t10
    },
    {
        "nombre": "U2T14. Triángulos",
        "funcion": u2t14
    },
    {
        "nombre": "U2T15. Calculadora",
        "funcion": u2t15
    }
]