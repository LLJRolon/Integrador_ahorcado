import tkinter
from PIL import Image, ImageTk

def perder():
    label_fondo.config(image=imagen_d)
    label_fondo.Image = imagen_d


ventana = tkinter.Tk()
ventana.title("Juego del ahorcado")
ventana.geometry("1366x768")

#Imagenes

imagen_fondo = Image.open("verdugo.png").resize((1366, 768))
fondo = ImageTk.PhotoImage(imagen_fondo)

imagen_d = Image.open("verdugo_D.png").resize((1366, 768))
fondo_d = ImageTk.PhotoImage(imagen_d)


label_fondo = tkinter.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

boton_perder = tkinter.Button(ventana, text="Perder", command=perder)
boton_perder.place(x=260, y=180)

#label_texto = tkinter.Label(ventana, text="Juego del Ahorcado", font=("Arial", 20), bg= "white")
#label_texto.place(x=600, y=20)

etiqueta = tkinter.Label(ventana, text = "Bienvenido al juego del ahorcado", font=("Arial", 20), bg= "white")
etiqueta.place(x = 400, y = 20)

boton_iniciar = tkinter.Button(ventana, text = "Iniciar juego")
boton_iniciar.place(x = 450, y = 200)

#letra_elegida = tkinter.Entry(ventana, font = "Helvetica 20")    input con la letra
#letra_elegida.grid(row=3, column= 2)



ventana.mainloop()