import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame
pygame.mixer.init()

# - - - - - - - - - - - - -- funciones de la logica - - --- -- - - - - - - -- - -

CATEGORIAS = {
    "Animales": ["ornitorrinco", "murcielago", "hipopotamo", "cocodrilo", "camaleon", "rinoceronte", "perezoso", "chimpance", "avestruz", "armadillo"],
    "Pokemons": ["pikachu", "charizard", "bulbasaur", "squirtle", "jigglypuff", "meowth", "mewtwo", "eevee", "snorlax", "gengar"],
    "Dragon-Ball Z": ["goku", "vegeta", "gohan", "piccolo", "krillin", "trunks", "freezer", "cell", "majin buu", "android 18", "android 17", "yamcha", "nappa", "raditz", "broly", "bardock", "dabura", "zarbon", "dodoria"],
    "Personajes de los Simpson": ["homero", "marge", "bart", "lisa", "maggie", "abuelo", "milhouse", "nelson", "moe", "apu", "burns", "smithers", "ned flanders", "rod", "todd", "krusty", "ralph", "edna", "willie", "lenny"],
    "Juegos": ["minecraft", "fortnite", "gta v", "call of duty", "fifa", "league of legends", "valorant", "among us", "the sims", "zelda", "super mario", "pokemon", "roblox", "counter strike", "elden ring", "god of war"],
    "Colores": ["rojo", "azul", "verde", "amarillo", "naranja", "violeta", "rosado", "negro", "blanco", "gris", "marron", "celeste", "turquesa", "dorado", "plateado"],
    "Comidas argentinas": ["asado", "empanadas", "milanesa", "choripan", "locro", "humita", "mate", "facturas", "pizzas", "fugazzeta", "canelones", "dulce de leche", "helado", "alfajores"],
    "Personajes de juegos": ["mario", "link", "sonic", "pac man", "kratos", "samus aran", "lara croft", "master chief", "pikachu", "leon scott kennedy", "arthur morgan", "tony hawk", "megaman", "jhon marston", "alyx vance", "nathan drake", "geralt de rivia", "steve", "villager"],
    "Animes": ["naruto", "dragon ball z", "one piece", "attack on titan", "hunter x hunter", "bleach", "fullmetal alchemist", "death note", "demon slayer", "my hero academia", "tokyo ghoul", "neon genesis evangelion", "sailor moon", "fairy tail", "jojos bizarre adventure"],
    "Peliculas": ["el padrino", "titanic", "la guerra de las galaxias", "batman", "avengers endgame", "el origen", "forrest gump", "matrix", "el señor de los anillos", "gladiador", "el club de la pelea"]

}
# - - - - - -- - - - - variables globales - - - - - - - - - - -
categoria_selec = ""
vidas = 6
palabra_secreta = ""
letras_adivinadas = [" "]
mensaje_estado = ""


pygame.mixer.music.load("musica_fondo.mp3")
pygame.mixer.music.play(-1)                         # el -1 hace el bucle infinito

sonido_correcto = pygame.mixer.Sound("correcto.mp3")
sonido_error = pygame.mixer.Sound("huh.mp3")
sonido_corazon = pygame.mixer.Sound("corazon.mp3")
musica_victoria = pygame.mixer.Sound("musica_victoria.mp3")
musica_derrota = pygame.mixer.Sound("musica_derrota.mp3")


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

    pygame.mixer.music.stop()
    pygame.mixer.music.load("musica_partida.mp3")
    pygame.mixer.music.play(-1)
    letras_adivinadas = [" "]
    vidas = 6

    label_fondo.config(image=fondo_iniciar_partida)
    label_fondo.image = fondo_iniciar_partida 

    palabra_categoria = CATEGORIAS[categoria_selec]
    palabra_secreta = random.choice(palabra_categoria)
    #frame_vidas.place(x = 400, y = 600)

    
    etiqueta_bienvenido.place_forget()
    letra_user.place(x=100, y=550)
    boton_enviar_letra.place(x=100, y=600)
    etiqueta_final.config(bg = "white")
    etiqueta_final.place(x=400, y=50)
    mensaje_estado.place(x=550, y=150)
    boton_reiniciar.place(x=100, y=650)
    mensaje_estado.config(text = "Espero sepas lo que haces...")
    

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
    pygame.mixer.music.stop()
    sonido_corazon.stop()
    musica_victoria.play()
    label_fondo.config(image=fondo_v)
    label_fondo.image = fondo_v
    letra_user.config(state="disable")
    boton_enviar_letra.config(state="disable")
    mensaje_estado.config(text = "Felicidades, ganaste a Python! \nSalvaste al programdor", fg = "green", bg = "white")
    mensaje_estado.place(x = 550, y = 100)


def perder():
    global palabra_secreta
    pygame.mixer.music.stop()
    musica_derrota.play()
    label_fondo.config(image=fondo_d)
    label_fondo.image = fondo_d
    letra_user.config(state="disabled")
    boton_enviar_letra.config(state="disabled")
    mensaje_estado.config(text = f"Mal ahí, no pudiste contra Python\nla palabra era {palabra_secreta}.", fg = "red")
    mensaje_estado.place(x = 450, y = 160)
    
    
def reiniciar_juego():
    global mensaje_estado, vidas, letras_adivinadas, palabra_secreta, categoria_selec
    
    label_fondo.config(image = fondo)
    musica_derrota.stop()
    musica_victoria.stop()
    pygame.mixer.music.load("musica_fondo.mp3")
    pygame.mixer.music.play(-1)

    mensaje_estado.config(text = "Elegí lo que mas sepas \npara salvar al programador", fg = "black")
    mensaje_estado.place(x = 570, y = 100)
    etiqueta_final.config(text = "")
    vidas = 6
    letras_adivinadas = [" "]
    palabra_secreta = ""
    categoria_selec = ""
    
    letras_usadas.place_forget()
    letra_user.place_forget()
    boton_enviar_letra.place_forget()
    etiqueta_final.place_forget()
    boton_reiniciar.place_forget()
    etiqueta_bienvenido.place(x = 400, y = 20)
    #frame_vidas.config(text = f"Tenes {vidas} intentos.")
    letra_user.delete(0, tk.END)
    letra_user.config(state = "disable")
    boton_enviar_letra.config(state = "disable")
    frame_categorias.place(x = 550, y = 200)
    #frame_vidas.place_forget()


def adivinar_letra():
    global vidas

    letra = letra_user.get().lower()
    letra_user.delete(0, tk.END)

    if letra == "" or letra == " " or not letra.isalpha():
        return

    if letra in letras_adivinadas:
        return
    letras_adivinadas.append(letra)    
    letras_usadas.config(text = "Letras usadas:" + " ".join(letras_adivinadas), font = ("terminal", 16))
    letras_usadas.place(x = 100, y = 500)

    if letra not in palabra_secreta:
        vidas -= 1
        sonido_error.play()

        if vidas == 5:
            label_fondo.config(image = vida_5)
        elif vidas == 4:
            label_fondo.config(image=vida_4)
        elif vidas == 3:
            label_fondo.config(image=vida_3)
        elif vidas == 2:
            label_fondo.config(image=vida_2)
        elif vidas == 1:
            label_fondo.config(image=vida_1)
            sonido_corazon.play(-1)
            
        elif vidas == 0:
            sonido_corazon.stop()
            perder()
    else:
        sonido_correcto.play()
        if all(e in letras_adivinadas or letra == " " for e in palabra_secreta):
            ganar()
            
    #frame_vidas.config(text = f"Tenes {vidas} intentos.")

    mostrar_palabra()

# - - - - - -- - - -- - - tkinter - - -- - - - - - - -- - - - -


ventana = tk.Tk()
ventana.title("Juego del ahorcado")
ventana.state("zoomed")


# Imagenes
imagen_fondo = Image.open("verdugo_nuevo.png").resize((1266, 668))
fondo = ImageTk.PhotoImage(imagen_fondo)

imagen_iniciar_partida = Image.open("verdugo_6.png").resize((1266, 668))
fondo_iniciar_partida = ImageTk.PhotoImage(imagen_iniciar_partida)

#imagen_6_vidas = Image.open("verdugo_6.png").resize((1266, 6680))
#vida_6 = ImageTk.PhotoImage(imagen_6_vidas)

imagen_5_vidas= Image.open("verdugo_5.png").resize((1266, 668))
vida_5 = ImageTk.PhotoImage(imagen_5_vidas)

imagen_4_vidas = Image.open("verdugo_4.png").resize((1266, 668))
vida_4 = ImageTk.PhotoImage(imagen_4_vidas)

imagen_3_vidas = Image.open("verdugo_3.png").resize((1266, 668))
vida_3 = ImageTk.PhotoImage(imagen_3_vidas)

imagen_2_vidas = Image.open("verdugo_2.png").resize((1266, 668))
vida_2 = ImageTk.PhotoImage(imagen_2_vidas)

imagen_1_vida = Image.open("verdugo_1.png").resize((1266, 668))
vida_1 = ImageTk.PhotoImage(imagen_1_vida)


imagen_d = Image.open("verdugo_D.png").resize((1266, 668))
fondo_d = ImageTk.PhotoImage(imagen_d)

imagen_v = Image.open("verdugo_V.png").resize((1266, 668))
fondo_v = ImageTk.PhotoImage(imagen_v)

label_fondo = tk.Label(ventana, image=fondo)
label_fondo.image = fondo
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)


# - - - - - - - - - botones/mensajes - - - - - - - - -

etiqueta_bienvenido = tk.Label(ventana, text="Bienvenido al juego del ahorcado", font=("terminal", 23), fg = "white" ,bg = "black")
etiqueta_bienvenido.place(x=400, y=30)

etiqueta_final = tk.Label(ventana, text = "", font = ("Arial, 20"))
etiqueta_final.place()

letras_usadas = tk.Label(ventana, text = "", font = "terminal, 10")
letras_usadas.place()

mensaje_estado = tk.Label(ventana, text = "Elegí lo que mas sepas \npara salvar al programador", font = ("terminal", 20), fg = "black", bg = "white")
mensaje_estado.place(x = 570, y = 100)

frame_categorias = tk.Frame(ventana, bg = "white")
frame_categorias.place(x = 550, y = 200)

frame_opciones = tk.Frame(ventana)
frame_opciones.place(x = 400, y = 100)

#boton_ganar = tk.Button(frame_opciones, text = "ganar", command = ganar)
#boton_ganar.pack(padx = 10, pady = 10)

#boton_perder = tk.Button(frame_opciones, text = "perder", command = perder)
#boton_perder.pack(padx = 30, pady = 10)

for id_c, nombre in enumerate(CATEGORIAS.keys()):
    boton = tk.Button(frame_categorias, text = nombre, command = lambda c = nombre: seleccionar_categoria(c), bg = "white")
    boton.grid(row = id_c, column = 0, padx = 6, pady = 5)

boton_enviar_letra = tk.Button(ventana, text="A ver si está . . . ", command=adivinar_letra)
boton_enviar_letra.place()

#frame_vidas = tk.Label(ventana, text = f"Tenes {vidas} intentos.", font = ("terminal", 19))
#frame_vidas.place()

letra_user = tk.Entry(ventana, font=("terminal", 23))
letra_user.place()

boton_reiniciar = tk.Button(ventana, text = "Reiniciar", command = reiniciar_juego)
boton_reiniciar.place()


ventana.mainloop()
