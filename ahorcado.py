import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk


# - - - - - - - - - - - - -- funciones de la logica - - --- -- - - - - - - -- - -

CATEGORIAS = {
    "Animales": ["ornitorrinco", "murcielago", "hipopotamo", "cocodrilo", "camaleon", "rinoceronte", "perezoso", "chimpance", "avestruz", "armadillo"],
    "Pokemons": ["pikachu", "charizard", "bulbasaur", "squirtle", "jigglypuff", "meowth", "mewtwo", "eevee", "snorlax", "gengar"],
    "Dragon-Ball Z": ["goku", "vegeta", "gohan", "piccolo", "krillin", "trunks", "frieza", "cell", "majin buu", "android 18", "android 17", "yamcha", "nappa", "raditz", "broly", "bardock", "dabura", "zarbon", "dodoria"],
    "Personajes de los Simpson": ["homero", "marge", "bart", "lisa", "maggie", "abuelo", "milhouse", "nelson", "moe", "apu", "burns", "smithers", "ned", "rod", "todd", "krusty", "ralph", "edna", "willie", "lenny"],
    "Juegos": ["minecraft", "fortnite", "gta v", "call of duty", "fifa", "league of legends", "valorant", "among us", "the sims", "zelda", "super mario", "pokemon", "roblox", "counter strike", "elden ring"],
    "Colores": ["rojo", "azul", "verde", "amarillo", "naranja", "violeta", "rosa", "negro", "blanco", "gris", "marron", "celeste", "turquesa", "dorado", "plateado"],
    "Comidas argentinas": ["asado", "empanadas", "milanesa", "choripán", "locro", "humita", "mate", "facturas", "pizzas", "fugazzeta", "canelones", "dulce de leche", "helado", "alfajores"],
    "Personajes de juegos": ["mario", "link", "sonic", "pac man", "kratos", "samus aran", "lara croft", "master chief", "pikachu", "riku", "cloud strife", "arthur morgan", "tony hawk", "megaman", "mewtwo", "alex vance", "nathan drake", "geralt de rivia", "isaac clarke", "villager"],
    "Animes": ["naruto", "dragon ball z", "one piece", "attack on titan", "hunter x hunter", "bleach", "fullmetal alchemist", "death note", "demon slayer", "my hero academia", "tokyo ghoul", "neon genesis evangelion", "sailor moon", "fairy tail", "jojo's bizarre adventure"],
    "Peliculas": ["the godfather", "titanic", "star wars", "the dark knight", "avengers: endgame", "inception", "forrest gump", "pulp fiction", "the matrix", "the lord of the rings: the fellowship of the ring", "the shawshank redemption", "gladiator", "jurassic park", "back to the future", "schindler's list", "the silence of the lambs", "avatar", "joker", "parasite", "fight club"],

}
# - - - - - -- - - - - variables globales - - - - - - - - - - -
categoria_selec = ""
vidas = 6
palabra_secreta = ""
letras_adivinadas = []
mensaje_estado = ""


def habilitar_interfaz():
    letra_user.config(state="normal")
    boton_enviar_letra.config(state="normal")
    label_fondo.config(image=imagen_fondo)
    label_fondo.image = imagen_fondo

def mostrar_palabra():                                    # Función para mostrar el estado actual de la palabra
    resultado = ""
    for letra in palabra_secreta:
        if letra == " ":
            resultado += "  "
        elif letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    etiqueta_final.config(text=resultado)

    return resultado



def iniciar_juego():
    global vidas, palabra_secreta, letras_adivinadas

    letras_adivinadas = []
    vidas = 6
    
    palabra_categoria = CATEGORIAS[categoria_selec]
    palabra_secreta = random.choice(palabra_categoria)
    frame_vidas.place(x = 400, y = 600)

    etiqueta.place_forget()
    letra_user.place(x=100, y=550)
    boton_enviar_letra.place(x=100, y=600)
    etiqueta_final.place(x=400, y=50)
    mensaje_estado.place(x=300, y=100)
    boton_reiniciar.place(x=100, y=650)
    mensaje_estado.config(text = "Espero sepas lo que haces . . . ")

    mostrar_palabra()
    habilitar_interfaz()


def seleccionar_categoria(nombre_categoria):
    global categoria_selec
    categoria_selec = nombre_categoria
    if categoria_selec in CATEGORIAS:
        frame_categorias.place_forget()
        #frame_opciones.place(x = 300, y = 200)
        iniciar_juego() 
    

def ganar():
    label_fondo.config(image=fondo_v)
    label_fondo.image = fondo_v
    letra_user.config(state="disable")
    boton_enviar_letra.config(state="disable")
    mensaje_estado.config(text = "Felicidades, ganaste a Python! Salvaste al programdor", fg = "green")


def perder():
    global palabra_secreta
    label_fondo.config(image=fondo_d)
    label_fondo.image = fondo_d
    letra_user.config(state="disabled")
    boton_enviar_letra.config(state="disabled")
    mensaje_estado.config(text = f"Mal ahí, no pudiste contra Python, la palabra era {palabra_secreta}.", fg = "red")
    
    
def reiniciar_juego():
    global mensaje_estado, vidas, letras_adivinadas, palabra_secreta, categoria_selec
    
    label_fondo.config(image = fondo)
    
    mensaje_estado.config(text = "Elegí lo que mas sepas para salvar al programador", fg = "black")
    etiqueta_final.config(text = "")
    vidas = 6
    letras_adivinadas = []
    palabra_secreta = ""
    categoria_selec = ""
        
    letra_user.place_forget()
    boton_enviar_letra.place_forget()
    etiqueta_final.place_forget()
    boton_reiniciar.place_forget()
    etiqueta.place(x = 400, y = 20)
    frame_vidas.config(text = f"Tenes {vidas} intentos.")
    letra_user.delete(0, tk.END)
    letra_user.config(state = "disable")
    boton_enviar_letra.config(state = "disable")
    frame_categorias.place(x = 400, y = 200)
    frame_vidas.place_forget()


def adivinar_letra():
    global vidas

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
    frame_vidas.config(text = f"Tenes {vidas} intentos.")

    mostrar_palabra()

# - - - - - -- - - -- - - tkinter - - -- - - - - - - -- - - - -


ventana = tk.Tk()
ventana.title("Juego del ahorcado")
ventana.geometry("1366x768")


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

imagen_corazon_lleno = Image.open("corazon_lleno.png").resize((200, 200))
corazon_lleno = ImageTk.PhotoImage(imagen_corazon_lleno)

imagen_corazon_vacio = Image.open("corazon_vacio.png")
corazon_vacio = ImageTk.PhotoImage(imagen_corazon_vacio)

# - - - - - - - - - botones/mensajes - - - - - - - - -

etiqueta = tk.Label(ventana, text="Bienvenido al juego del ahorcado", font=("terminal", 23))
etiqueta.place(x=400, y=20)

etiqueta_final = tk.Label(ventana, text = "", font = ("Arial, 20"))
etiqueta_final.place()


mensaje_estado = tk.Label(ventana, text = "Elegí lo que mas sepas para salvar al programador", font = ("terminal", 20), fg = "black")
mensaje_estado.place(x = 300, y = 100)

frame_categorias = tk.Frame(ventana)
frame_categorias.place(x = 550, y = 200)

frame_opciones = tk.Frame(ventana)

boton_salir = tk.Button(frame_opciones, text = "Salir", command = ventana.quit)
boton_salir.pack(padx = 300, pady = 100)

for id_c, nombre in enumerate(CATEGORIAS.keys()):
    boton = tk.Button(frame_categorias, text = nombre, command = lambda c = nombre: seleccionar_categoria(c))
    boton.grid(row = id_c, column = 0, padx = 6, pady = 5)

boton_enviar_letra = tk.Button(ventana, text="A ver si está . . . ", command=adivinar_letra)
boton_enviar_letra.place()

frame_vidas = tk.Label(ventana, text = f"Tenes {vidas} intentos.", font = ("terminal", 19))
frame_vidas.place()

letra_user = tk.Entry(ventana, font=("terminal", 23))
letra_user.place()

boton_reiniciar = tk.Button(ventana, text = "Reiniciar", command = reiniciar_juego)
boton_reiniciar.place()


ventana.mainloop()
