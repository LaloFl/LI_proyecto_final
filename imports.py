from os import system, name
from threading import enumerate

from u1t1_portada import main as u1t1


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
    }
]