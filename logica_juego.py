
import random

palabras = ["prueba", "otra prueba"]
palabra_secreta = random.choice(palabras)                # Lista de palabras
letras_adivinadas = []
vidas = 6

# Función para mostrar el estado actual de la palabra
def mostrar_palabra():
    resultado = ""                                    
    for letra in palabra_secreta:
        if letra == " ":
            resultado += "  "
        elif letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

while vidas > 0:
    print("Palabra:", mostrar_palabra())
    print("Intentos restantes:", vidas)
    letra_user = input("Adiviná una letra: ").lower()

    if letra_user in letras_adivinadas:
        print("Ya la adivinaste.")
    elif letra_user in palabra_secreta:
        letras_adivinadas.append(letra_user)
    else:
        letras_adivinadas.append(letra_user)
        vidas -= 1
    if all(e in letras_adivinadas or e == " " for e in palabra_secreta):
        print("Ganaste!")
        break
else:
    print("Perdiste. La palabra era: ", palabra_secreta)
