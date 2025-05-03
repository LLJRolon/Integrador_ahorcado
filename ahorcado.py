import tkinter as tk
import random
from PIL import Image, ImageTk


# - - - - - - - - - - - - -- funciones de la logica - - --- -- - - - - - - -- - -

CATEGORIAS = {
    "Animales": ["ornitorrinco", "murcielago", "hipopotamo", "cocodrilo", "camaleon", "rinoceronte", "perezoso", "chimpance", "avestruz", "armadillo"],
    "Pokemons": ["pikachu", "charizard", "bulbasaur", "squirtle", "jigglypuff", "meowth", "mewtwo", "eevee", "snorlax", "gengar"],
    "Dragon-Ball Z": ["goku", "vegeta", "gohan", "piccolo", "krillin", "trunks", "frieza", "cell", "majin buu", "android 18", "android 17", "yamcha", "tien", "nappa", "raditz", "broly", "bardock", "dabura", "zarbon", "dodoria"],
    "Personajes de los Simpson": ["homero", "marge", "bart", "lisa", "maggie", "abuelo", "milhouse", "nelson", "moe", "apu", "burns", "smithers", "ned", "rod", "todd", "krusty", "ralph", "edna", "willie", "lenny"],
    "Juegos": ["minecraft", "fortnite", "gta v", "call of duty", "fifa", "league of legends", "valorant", "among us", "the sims", "zelda", "super mario", "pokemon", "roblox", "counter strike", "elden ring"],
    "Colores": ["rojo", "azul", "verde", "amarillo", "naranja", "violeta", "rosa", "negro", "blanco", "gris", "marrón", "celeste", "turquesa", "dorado", "plateado"],
    "Comidas argentinas": ["asado", "empanadas", "milanesa", "choripán", "provoleta", "locro", "humita", "mate", "facturas", "pizzas", "fugazzeta", "canelones", "dulce de leche", "helado", "alfajores"],
    "Personajes de juegos": ["mario", "link", "sonic", "pac man", "kratos", "samus aran", "lara croft", "master chief", "pikachu", "riku", "cloud strife", "arthur morgan", "tony hawk", "megaman", "mewtwo", "alex vance", "nathan drake", "geralt de rivia", "isaac clarke", "villager"],
    "Animes": ["naruto", "dragon ball z", "one piece", "attack on titan", "hunter x hunter", "bleach", "fullmetal alchemist", "death note", "demon slayer", "my hero academia", "tokyo ghoul", "neon genesis evangelion", "sailor moon", "fairy tail", "jojo's bizarre adventure"],
    "Peliculas": ["the godfather", "titanic", "star wars", "the dark knight", "avengers: endgame", "inception", "forrest gump", "pulp fiction", "the matrix", "the lord of the rings: the fellowship of the ring", "the shawshank redemption", "gladiator", "jurassic park", "back to the future", "schindler's list", "the silence of the lambs", "avatar", "joker", "parasite", "fight club"],

}

categoria_selec = ""

vidas = 6
palabra_secreta = ""
letras_adivinadas = []


def seleccionar_categoria(**categoria):
    categoria_selec = categoria.get("categorias")
    if categoria_selec:
        palabra_categoria = CATEGORIAS.get(categoria_selec)

    if palabra_categoria:
        palabra_secreta = random.choice(palabra_categoria)
        iniciar_juego(palabra_secreta)
    else:
        print(f"Categoría '{categoria_selec}' no encontrada.")


def habilitar_interfaz():
    letra_user.config(state="normal")
    boton_enviar_letra.config(state="normal")


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
    etiqueta.config(text=resultado)

    return resultado


def iniciar_juego():
    global vidas, palabra_secreta, letras_adivinadas

    letras_adivinadas = []
    vidas = 6

    palabra_categoria = CATEGORIAS[categoria_selec]
    palabra_secreta = random.choice(palabra_categoria)

    mostrar_palabra()
    habilitar_interfaz()


def ganar():
    label_fondo.config(image=fondo_v)
    label_fondo.image = fondo_v
    letra_user.config(state="disable")
    boton_enviar_letra.config(state="disable")


def perder():
    label_fondo.config(image=fondo_d)
    label_fondo.image = fondo_d
    letra_user.config(state="disabled")
    boton_enviar_letra.config(state="disabled")


def adivinar_letra():
    vidas = 6

    letra = letra_user.get().lower()
    letra_user.delete(0, tk.END)

    if letra in letras_adivinadas:
        return
    letras_adivinadas.append(letra)

    if letra not in palabra_secreta:
        vidas -= 1
        if vidas == 0:
            perder()
    else:
        if all(e in letras_adivinadas or letra == " " for e in palabra_secreta):
            ganar()

    mostrar_palabra()

# - - - - - -- - - -- - - Tkinter - - -- - - - - - - -- - - - -


ventana = tk.Tk()
ventana.title("Juego del ahorcado")
ventana.geometry("1366x768")

boton_animales = tk.Button(ventana, text = "Animales", command = lambda: seleccionar_categoria(categoria="Animales"))

boton_animales.place(x=200, y= 200)

letra_user = tk.Entry(ventana, font=("Arial", 20))
letra_user.place(x=100, y=200)

boton_enviar_letra = tk.Button(
    ventana, text="A ver si es...", command=adivinar_letra)
boton_enviar_letra.place(x=100, y=250)

boton_iniciar = tk.Button(ventana, text="Iniciar juego", command=iniciar_juego)
boton_iniciar.place(x=450, y=200)

# Imagenes
imagen_fondo = Image.open("verdugo.png").resize((1366, 768))
fondo = ImageTk.PhotoImage(imagen_fondo)

imagen_d = Image.open("verdugo_D.png").resize((1366, 768))
fondo_d = ImageTk.PhotoImage(imagen_d)

imagen_v = Image.open("verdugo_V.png").resize((1366, 768))
fondo_v = ImageTk.PhotoImage(imagen_v)

label_fondo = tk.Label(ventana, image=fondo)
label_fondo.image = fondo
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
'''
boton_perder = tk.Button(ventana, text="Perder",
                         command=perder)  # test imagen de perder
boton_perder.place(x=260, y=180)

boton_ganar = tk.Button(ventana, text="Ganar",
                        command=ganar)  # test imagen de ganar
boton_ganar.place(x=460, y=180)
'''
etiqueta = tk.Label(
    ventana, text="Bienvenido al juego del ahorcado", font=("Arial", 20))
etiqueta.place(x=400, y=20)

ventana.mainloop()
